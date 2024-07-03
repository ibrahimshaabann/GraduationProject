# Digital Copyrights Project Documentation

## Introduction

### Project Objectives

- Ensure privacy for content owners by implementing measures to secure personal content, fostering a sense of trust and privacy within the online platform.
- Detect and prevent unauthorized sharing by creating a robust system that safeguards digital content, including photos, videos, and audio, from unauthorized use. Incorporate advanced features such as content analysis and reporting to actively identify and mitigate instances of unauthorized content sharing.
- Establish a user-friendly moderation system that allows users to report violations easily and ensures prompt, effective action against infringing content.

### Approaches and Methodology

The development of Digital Copyrights involves a comprehensive set of approaches and methodologies to ensure the successful implementation of the copyright protection system. The key strategies include:

#### User-Centric Design

- Adopt a user-centric approach to design and development, focusing on the end-user experience. Gather user feedback iteratively to refine features and enhance usability.

#### Privacy-First Principles

- Prioritize user privacy by implementing robust encryption mechanisms, ensuring that personal content remains secure and accessible only to authorized users.

#### Perceptual Hashing for Content Matching

- Deploy perceptual hashing techniques for the detection of visually or auditory similar content. This involves capturing unique visual and auditory characteristics to generate perceptual hashes for content analysis.

#### BK-Tree for Efficient Similarity Search

- Utilize BK-Tree data structure to enhance the efficiency of searching for visually or auditory similar content. This approach minimizes the number of distance calculations required for similarity search.

#### Reporting and Moderation System

- Develop a reporting and moderation system where users can easily report content violations. Enable content moderators to review reported content and take appropriate actions, including content removal and user warnings.

#### Scalability Measures

- Implement measures to handle a growing user base and content library efficiently. Ensure that the system can scale seamlessly to accommodate increased demand.

### Project Plan and Management

1. **Project Initiation** (November 1, 2023 - November 15, 2023)
   - Define Project Scope and Objectives.
   - Assemble Project Team and Assign Roles.
   - Conduct Initial Kick-off Meeting.

2. **Requirements Gathering and Analysis** (November 16, 2023 - December 15, 2023)
   - Collect and Document Functional and Non-functional Requirements.
   - Conduct Stakeholder Meetings for Clarifications.
   - Prioritize Requirements and Finalize Scope.

3. **System Design and Architecture** (December 16, 2023 - February 1, 2024)
   - Design System Architecture.
   - Develop Detailed Design for Subsystems (Authentication, Content Management, Perceptual Hashing, Reporting, and Moderation).
   - Review and Validate Design with Stakeholders.

4. **Documentation** (February 1, 2024 - February 12, 2024)
   - Prepare System Documentation.
   - Develop User Manuals for Platform Extension and Privacy Tool.
   - Create Technical Documentation for Maintenance.

5. **Development** (February 13, 2024 - April 1, 2024)
   - Implement Authentication and Authorization Module.
   - Develop Content Upload and Storage Module.
   - Implement Perceptual Hashing for Content Analysis.
   - Integrate Reporting and Moderation System.

6. **Testing and Quality Assurance** (April 2, 2024 – April 17, 2024)
   - Implement User Acceptance Testing (UAT).
   - Address Bugs and Refine Code.

7. **Privacy Tool Development** (April 3, 2024 - May 10, 2024)
   - Develop a User-Facing Privacy Tool.
   - Implement Features for Personal Content Management.
   - Ensure Compatibility with Different Devices.

8. **Final Testing and Debugging** (May 14, 2024 - May 25, 2024)
   - Comprehensive System Testing.
   - Address Any Remaining Bugs or Issues.
   - Verify the Performance and Security Measures.

9. **Deployment** (May 25, 2024 - June 1, 2024)
   - Deploy the Copyright Protection System and database on railway. Communication.

10. **Monitoring and Updates** (June 1, 2023 - January 6, 2024)
   - Implement Continuous Monitoring for Security.
   - Add more features like video and voice recognition
   - Regularly Update System Components.
   - Gather User Feedback for Future Enhancements.

### Deliverables

- **Social Media Platform Extension (Deliverable 1):** Integration of Digital Copyrights onto Targeted Social Media Platforms. Seamless Functionality for Copyright Protection.
- **User Privacy Tool (Deliverable 2):** User-Friendly Tool for Managing Personal Content Privacy. Options for Secure Content Uploads, Permissions, and Privacy Settings.

## Analysis

### Introduction

#### Purpose

Creating an API that helps detect and prevent the posting of copyrighted content on social media platforms is a complex and challenging project. It involves several components, including image recognition copyright detection and integration with our social media app.

#### Document Conventions

The Document is prepared using Microsoft Word 2019 and has used the font type ‘Times New Roman’. The fixed font size that has been used to type this Document is 12pt with 1.5 line spacing. It has used the bold property to set the headings and of the document. Use case scenario is written according to Alistair Cockburn’s template. UML diagrams have been created according to UML 2.0 standards. Standard IEEE template is the template used to organize the appearance of the document and its flow.

#### Intended Audience and Reading Suggestions

The reader and audience for whom this document is designed include developers, project supervisor, owners of social applications platforms, testers, and documentation writers.

### Overall Description

#### Product Scope

The Copyright API which is going to be implemented for detection and prevention of the posting of copyrighted content on social media has the following aspects:

- Copyright information retrieval: Provide the ability to retrieve detailed information about copyrighted works, including data such as title, author, publication date, and copyright status.
- Rights and Permissions: Include information on rights and permissions associated with copyrighted works, offer a way to check if a user has the right to use or reproduce a specific work.
- Notification and Alerts: Implement a notification system to alert users about changes in copyright status or licensing agreements for specific works.
- Compliance with copyright laws: Ensure that the API complies with relevant copyright laws and regulations, both at national and international levels.
- Usage Analytics: Provide analytics features to help users understand how copyrighted materials are being used and accessed.

#### Product Functions

The system functions include:

- **User Registration:** Allow users to register on the Digital Copyright Protection System.
- **User Authentication:** Allow users to authenticate on the Digital Copyright Protection System.
- **Uploading Photos:** When a user uploads a photo, the API hashes it and searches for identical photos in the database using perceptual hashing.
- **Detecting Same Photos:** Notifies the user if another user uploads the same photo, allowing the user to decide whether to keep or remove the copyrighted content.
- **Copyright Information Retrieval:** Provides detailed reports on copyrighted works.
- **Removing Copyrighted Content:** Deletes the photo from the database if the owner chooses to remove it.
- **Keeping Copyrighted Content:** Stores the photo in the database if the owner chooses to keep it.

#### User Classes and Characteristics

There are three user classes:

I. **Users:** Owners of digital content who use the API to manage and protect their copyrighted material.
II. **Our Implemented Social Media App:** Manages and tracks copyrights for published material.
III. **Developers:** Integrate the API into applications, websites, or systems to automate copyright-related processes.

#### Operating Environment

**Hardware and Software Requirements:**

- **Hardware:** Compatible with all computers and mobile devices using our implemented social app or future platforms.
- **Software:** Designed to run on any social media platform, integrated with our app using Django (Python web framework) and PostgreSQL 3.17.2 edition.

#### Design and Implementation Constraints

To ensure reliability and compliance, the following constraints are applied:

- Legal and Regulatory Compliance: Ensure adherence to copyright laws and prevent unauthorized use.
- Authentication and Authorization: Restrict access based on user roles and permissions.
- Scalability and Performance: Optimize for large-scale usage, consider caching and GPU databases for performance enhancement.
- Documentation and Education: Provide comprehensive developer documentation and user manuals.
- Interoperability: Ensure compatibility with common programming languages and frameworks.

#### User Documentation

User manuals will provide clear instructions for interacting with the API in a simple, understandable language.

#### Assumptions and Dependencies

Assumptions include user compliance with copyright laws, accurate information provided by the API, authorized user interactions, stable internet connectivity, integration with compatible systems, reliance on third-party authentication providers, adherence to data privacy regulations, and secure communication protocols.

### External Interface Requirements

#### User Interfaces

The user interface should be intuitive and easy to navigate, with features such as:

- User-friendly dashboard for content management.
- Clear notifications for copyright violations.
- Reporting tools for users to flag unauthorized content.

#### Hardware Interfaces

The system should interface with the following hardware components:

- **Storage Devices:** Interface with storage devices such as hard drives, solid-state drives (SSDs), or cloud storage services to store uploaded content, analysis results, and other system data.
- **Network Devices:** Interface with network devices such as routers, switches, and firewalls to facilitate network communication between system components and external services.
- **Processing Units:** Interface with processing units such as central processing units (CPUs), graphics processing units (GPUs), or specialized hardware accelerators for performing computationally intensive tasks such as content analysis and perceptual hashing.
- **Backup Devices:** Interface with backup devices such as tape drives, external hard drives
