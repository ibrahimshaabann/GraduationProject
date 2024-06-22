# Project Documentation

## Project Idea

The project aims to create a copyright protection system for digital content (photos, videos, and audio) shared on a platform. The system will provide content owners with tools to protect their personal content, ensure its privacy, and detect unauthorized sharing. Key features include encryption, watermarking, content analysis, reporting, and moderation.

## Requirements

### Functional Requirements

1. User Authentication and Authorization
   - Users must register and authenticate to access the platform.
   - Different user roles (content owners, regular users) with varying privileges.

2. Content Upload and Storage
   - Users can upload personal photos, videos, and audio files.
   - Content is securely stored with encryption at rest.

3. Content Encryption
   - Personal content (photos, videos, audio) is encrypted using AES encryption.
   - Authorized users can decrypt content for viewing or download.

4. Perceptual Hashing
   - Implement perceptual hashing for detecting visually similar or near-duplicate content across images, videos, and audio.
   - Capture visual or auditory characteristics of content to generate perceptual hashes.
   - Use perceptual hashing to identify similarities in uploaded content with existing content.
   - Visually or auditorily similar content is detected based on perceptual hash matches.

5. Content Analysis
   - Implement image and audio analysis for identifying personal content.
   - Detection of personal content during uploads and downloads.

6. Audio Watermarking
   - Embed ownership information and copyright data within audio files.
   - Use audio watermarking to assert ownership and copyright.
   - Detect unauthorized sharing of audio content through the presence of watermarks.

7. Audio Fingerprinting (Dejavu)
   - Implement audio fingerprinting using the Dejavu library for audio recognition.
   - Detect copyrighted audio content and unauthorized uploads.
   
8. Reporting and Moderation
   - Users can report content that violates platform policies.
   - Content moderation to review reported content and take action.

9. Image Hashing
   - Generate image hashes for duplicate detection.
   - Detect identical copies of images based on hash values.

10. Secure Storage
    - Ensure personal content is stored securely.
    - Encryption keys are managed securely.


### Non-Functional Requirements

1. Security and Privacy
   - Protection of personal content through encryption.
   - Robust detection of unauthorized sharing.
   - Compliance with copyright and privacy laws.

2. Performance
   - Efficient handling of content uploads and downloads.
   - Fast image hashing and content analysis.

3. Usability
   - User-friendly interface for content management.
   - Clear copyright and privacy policies.

4. Scalability
   - Ability to handle a growing user base and content library.

## Frameworks and Technologies

- Backend Framework: Django (Python)
- Frontend Framework: Flutter
- Database: PostgreSQL
- Encryption: AES (Advanced Encryption Standard)
- Content Analysis: [Specify the image and audio analysis libraries or tools]

## Encryption Algorithms

- AES (Advanced Encryption Standard) for encrypting photos, videos, and audio.
- Use of AES-CTR or AES-GCM modes for secure encryption and decryption.
- Encryption keys stored securely and accessible only to authorized users.

## Content Analysis

- Content analysis involves using image and audio analysis libraries or tools to identify personal content.
- Image analysis detects personal photos based on visual cues and unique features.
- Audio analysis detects personal audio based on characteristics such as voice recognition.
- Analysis is performed during content uploads and downloads to detect unauthorized sharing.

## Reporting and Moderation

- Users can report content that violates platform policies or infringes on copyrights.
- Reported content is reviewed by content moderators.
- Action is taken to address violations, including content removal and user warnings.


## Secure Storage

- Personal content is stored in a secure manner, with encryption at rest.
- Strong access controls to prevent unauthorized access to content.
- Regular security audits and updates to ensure data security.

---

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

