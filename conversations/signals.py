# conversations/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Conversation
import nltk

nltk.download('punkt')

@receiver(pre_save, sender=Conversation)
def generate_summary(sender, instance, **kwargs):
    if not instance.summary:
        instance.summary = summarize_text(instance.content)

def summarize_text(text):
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return ' '.join(sentences[:3])  # Simple summary: first 3 sentences
