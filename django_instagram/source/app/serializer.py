from rest_framework import serializers
from app.models import Post, PostComment, PostLike, User, UserFollow , Notification


class UserSerializer(serializers.ModelSerializer):
   # groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'password','bio' ,'image_url']

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    bio = serializers.CharField()
    image_url = serializers.ImageField(required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    """
    This setup ensures that when you pass user data to NotificationSerializer, 
    it expects a primary key value (pk) that corresponds to an existing User instance.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Notification
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = '__all__'
    
    title = serializers.CharField()
    description = serializers.CharField()
    image_url = serializers.ImageField(required=False)
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.user.id == validated_data["user"].id:
            return super().update(instance, validated_data)
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        BASE_URL = 'https://graduationproject-production-a5f5.up.railway.app/media/'  
        representation['image_url'] = BASE_URL + str(instance.image_url)
        return representation



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

    comment_text = serializers.CharField(max_length=264)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    def save(self, **kwargs):
        print(kwargs)
        self.post = kwargs["post"]
        return super().save(**kwargs)


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = "__all__"

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    follows_id = serializers.PrimaryKeyRelatedField(read_only=True)
