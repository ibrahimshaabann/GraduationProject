from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import dhash
from .serializer import NotificationSerializer
from .models import Post
from .utils import bktree

@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if created and instance.image_url:
        try:
            img = Image.open(instance.image_url)
            row, col = dhash.dhash_row_col(img)
            image_hash = dhash.format_hex(row, col)
            instance.image_hash = image_hash
            instance.save()

            # Check for similar images
            similar_posts = bktree.query(image_hash, tolerance=3)
            print("#" * 30)
            print(f"\n\n\similar posts value:{similar_posts}\n\n\n")
            print("#" * 30)

            notification_data = None
            if similar_posts:
                print("*" * 30)
                print(f"\n\n\nsimilarrrrrrrrrrrrrrr!!!!\n\n\n")
                print("*" * 30)
                original_post_id = similar_posts[0][0]
                original_post = Post.objects.get(id=original_post_id)
                notification_data = {
                    'user': original_post.user.pk,
                    'post': instance.id,
                    'action_taken': None
                }

            if notification_data:
                notification_serializer = NotificationSerializer(data=notification_data)
                if notification_serializer.is_valid():
                    try:
                        notification_instance = notification_serializer.save()
                        print(f"Notification saved successfully: {notification_instance}")
                    except Exception as e:
                        print(f"Error saving notification: {e}")
                else:
                    print(f"Validation errors: {notification_serializer.errors}")

            bktree.insert(instance.image_hash, instance.id)

        except Exception as e:
            print(f"Error processing image: {e}")
