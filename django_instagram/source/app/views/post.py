from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import PostSerializer
from ..utils import bktree
from rest_framework import generics, status
import dhash
from PIL import Image
from app.models import Post, PostComment, PostLike, User, UserFollow ,Post , Notification
from app.serializer import CommentSerializer, PostLikeSerializer, PostSerializer, UserFollowSerializer , NotificationSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class CreatePost(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
   
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = request.data.get('image_url')
        if image:
            img = Image.open(image)
            row, col = dhash.dhash_row_col(img)
            image_hash = dhash.format_hex(row, col)

            # Check for similar images
            similar_posts = bktree.query(image_hash, tolerance=3)
            if similar_posts:
                original_post = Post.objects.get(id=similar_posts[0][0])
                notification_data = {
                    'user': original_post.user,
                    'post': similar_posts,
                    'action_taken': request.data.get('action_taken')  # Assuming action_taken is passed in request data
                }
                notification_serializer = NotificationSerializer(data=notification_data)
                if notification_serializer.is_valid():
                    notification_serializer.save()

                action_taken = request.data.get('action_taken')
                if action_taken == 'keep':
                    post = serializer.save(user=self.request.user)
                    bktree.insert(post.image_hash, post.id)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "status": "Failed",
                        "message": "Similar image already exists",
                        "original_post": PostSerializer(original_post).data
                    }, status=status.HTTP_400_BAD_REQUEST)

        post = serializer.save(user=self.request.user)
        bktree.insert(post.image_hash, post.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrievePost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({ "success": True, "message": "updated post" })
        else:
            print(serializer.errors)
            return Response({ "success": False, "message": "error updating post" })

class DestroyPost(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk")
            post = Post.objects.get(id=pk)
            if post.user.id == request.user.id:
                self.perform_destroy(post)
                return Response({ "success": True, "message": "post deleted" })
            else:
                return Response({ "success": False, "message": "not enough permissions" })
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
        
class DeleteCopiedImage(generics.DestroyAPIView):
     permission_classes = [IsAuthenticated]
     queryset = Post.objects.all()
     serializer_class = PostSerializer

     def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            if instance.user == request.user:
                self.perform_destroy(instance)
                return Response({"status": "success ", "message": "Post deleted"}, status=status.HTTP_200_OK)
            else:
                # Check if the user has uploaded a similar image
                user_posts = Post.objects.filter(user=request.user)
                for user_post in user_posts:
                    if dhash.get_num_bits_different(int(user_post.image_hash, 16), int(instance.image_hash, 16)) <= 3:
                        self.perform_destroy(instance)
                        return Response({"status": "Failed ", "message": "Similar post deleted"}, status=status.HTTP_200_OK)
                
                return Response({"status": "Failed ", "message": "Not enough permissions"}, status=status.HTTP_403_FORBIDDEN)

# app/views/notification.py

class ListNotifications(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, seen=False)

class HandleNotification(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        notification = self.get_object()
        action_taken = request.data.get('action_taken')

        if action_taken == 'delete':
            # delete the duplicated post
            notification.post.delete()  
      

        # Mark notification as seen and action taken
        notification.seen = True
        notification.action_taken = True
        notification.save()

        return Response({"message": "Notification handled successfully"}, status=status.HTTP_200_OK)

class RetrieveUserPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
        user_posts = Post.objects.filter(user=request.user.id)
        serializer = self.serializer_class(user_posts, many=True)
        return Response({ "success": True, "posts": serializer.data })
    

class GetAllPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_posts = Post.objects.all()
        serializer = self.serializer_class(user_posts, many=True)
        return Response({ "success": True, "posts": serializer.data })


class LikePost(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            likes_list = PostLike.objects.filter(post=post)

            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = PostLikeSerializer(likes_list, many=True)
            return Response({ "success": True, "likes_list": serializer.data })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })

    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            new_post_like = PostLike.objects.get_or_create(user=request.user, post=post)
            if not new_post_like[1]:
                new_post_like[0].delete()
                return Response({ "success": True, "message": "post unliked" })
            else:
                return Response({ "success": True, "message": "post liked" })

        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
    

class CommentPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            context = {
                "request": request,
            }
            post = Post.objects.get(id=pk)
            comments = PostComment.objects.filter(post=post)
            print(comments)

            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = self.serializer_class(comments, many=True)
            return Response({ "success": True, "comments": serializer.data })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })

    def post(self, request, pk):
        try:
            context = {
                "request": request,
            }
            post = Post.objects.get(id=pk)
            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = self.serializer_class(context=context, data=request.data)
            if serializer.is_valid():
                serializer.save(post=post)
                return Response({ "success": True, "message": "comment added" })
            else:
                print(serializer.errors)
                return Response({ "success": False, "message": "error adding a comment" })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })


class FollowUser(APIView):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        following = UserFollow.objects.filter(user=request.user)
        followers = UserFollow.objects.filter(follows=request.user)

        following_serializer = UserFollowSerializer(following, many=True)
        followers_serializer = UserFollowSerializer(followers, many=True)
        return Response({ "success": True, "following": following_serializer.data, "followers": followers_serializer.data })


    def post(self, request, pk):
        try:
            following_user = User.objects.get(id=pk)
            follow_user = UserFollow.objects.get_or_create(user=request.user, follows=following_user)
            if not follow_user[1]:
                follow_user[0].delete()
                return Response({ "success": True, "message": "unfollowed user" })
            else:
                return Response({ "success": True, "message": "followed user" })


        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "following user does not exist" })




