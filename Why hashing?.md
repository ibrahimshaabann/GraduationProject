# Some Notes

## Why we Prefer Perceptual hashing over invisible watermarking?

### Watermarking
- **Considerations :**

  1. **Visibility:** Some users may find visible watermarks obtrusive or detracting from the content's aesthetics.
  2. **Quality Impact:** Watermarking can introduce some quality degradation, especially if not applied carefully.
  3. **Removal Attempts:** While watermarks are challenging to remove, determined individuals with the right skills can still attempt to do so.

### Perceptual Hashing

- **Advantages:**

  1. **Content Recognition:** Perceptual hashing focuses on capturing visual or perceptual similarity between images. It is useful for detecting near-duplicate content.
  2. **Efficiency:** Perceptual hashing is often computationally efficient and can quickly identify similar images.
  3. **Discreetness:** Perceptual hashes are not visible to users, so they do not alter the content's appearance.

### Audio Watermarking and Fingerprinting

**Audio Watermarking:**

- *Ownership Assertion:* Audio watermarking is primarily used to assert ownership and copyright. It embeds ownership information into audio files, making it clear who owns the content.

- *Perceptibility:* Watermarks are typically imperceptible to the human ear, ensuring that the audio quality remains unaffected.

- *Detection Simplicity:* Detecting watermarks is relatively straightforward, as it involves checking for the presence of the watermark data within the audio file.

- *Use Case:* Audio watermarking is particularly useful for scenarios where copyright ownership needs to be established, and you want to deter unauthorized sharing or usage of audio content.

**Audio Fingerprinting:**

- *Content Recognition:* Audio fingerprinting focuses on recognizing specific audio content. It can identify copyrighted audio content, even if it has been altered, making it effective for content identification.

- *Versatility:* Fingerprinting can be used for various purposes, including copyright protection, content recognition, and audio matching.

- *Pattern Recognition:* Fingerprinting identifies audio based on unique characteristics, patterns, or signatures within the content.

- *Use Case:* Audio fingerprinting is valuable when you need to recognize and verify audio content, such as detecting copyrighted music or identifying unauthorized uploads.

**Preferred Option:**

Content Identification: Our project needs to recognize and verify audio content, such as detecting copyrighted music or identifying unauthorized uploads, audio fingerprinting is a better option. It excels at identifying and verifying specific audio content, making it the preferred choice for content recognition in our project.
