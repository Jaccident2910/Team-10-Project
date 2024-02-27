# Software Requirements Specification
## For the Technical Talent Finding System

Version 0.1  
Prepared by Jack Harris
Team 10 of the 2024 Oxford CompSci Second Year Group Design Practical  
created 2024/02/27

Table of Contents
=================
* [Revision History](#revision-history)
* 1 [Introduction](#1-introduction)
  * 1.1 [Document Purpose](#11-document-purpose)
  * 1.2 [Product Scope](#12-product-scope)
  * 1.3 [Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  * 1.4 [References](#14-references)
  * 1.5 [Document Overview](#15-document-overview)
* 2 [Product Overview](#2-product-overview)
  * 2.1 [Product Perspective](#21-product-perspective)
  * 2.2 [Product Functions](#22-product-functions)
  * 2.3 [Product Constraints](#23-product-constraints)
  * 2.4 [User Characteristics](#24-user-characteristics)
  * 2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
  * 2.6 [Apportioning of Requirements](#26-apportioning-of-requirements)
* 3 [Requirements](#3-requirements)
  * 3.1 [External Interfaces](#31-external-interfaces)
    * 3.1.1 [User Interfaces](#311-user-interfaces)
    * 3.1.2 [Hardware Interfaces](#312-hardware-interfaces)
    * 3.1.3 [Software Interfaces](#313-software-interfaces)
  * 3.2 [Functional](#32-functional)
  * 3.3 [Quality of Service](#33-quality-of-service)
    * 3.3.1 [Performance](#331-performance)
    * 3.3.2 [Security](#332-security)
    * 3.3.3 [Reliability](#333-reliability)
    * 3.3.4 [Availability](#334-availability)
  * 3.4 [Compliance](#34-compliance)
  * 3.5 [Design and Implementation](#35-design-and-implementation)
    * 3.5.1 [Installation](#351-installation)
    * 3.5.2 [Distribution](#352-distribution)
    * 3.5.3 [Maintainability](#353-maintainability)
    * 3.5.4 [Reusability](#354-reusability)
    * 3.5.5 [Portability](#355-portability)
    * 3.5.6 [Cost](#356-cost)
    * 3.5.7 [Deadline](#357-deadline)
    * 3.5.8 [Proof of Concept](#358-proof-of-concept)
* 4 [Verification](#4-verification)
* 5 [Appendixes](#5-appendixes)

## Revision History
| Name | Date    | Reason For Changes  | Version   |
| ---- | ------- | ------------------- | --------- |
|      |         |                     |           |
|      |         |                     |           |
|      |         |                     |           |

## 1. Introduction
This document will act as the specification from which Team 10 shall produce a talent finding system for Microsoft. This system will enable Microsoft to find talented individuals who would be suited to working in a software development role, and it will do so in ways specified in this document.

### 1.1 Document Purpose
The purpose of this document is twofold: to provide a specification from which the developers can produce the intended software, and to provide a specification of the system on which the developers and the client agree.

### 1.2 Product Scope
The purpose of the product is to enable Microsoft to find talented potential hires for graduate software development roles. It will do so by providing a series of puzzles which test algorithmic thinking and advanced coding, similar to those found on websites like [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/) and [AlgoExpert](https://www.algoexpert.io/product). It will also provide ranking metrics for the performance of the users of the system, alongside an overall ranking of the users. There will also be gamified elements which provide extrinsic rewards for the users.

### 1.3 Definitions, Acronyms and Abbreviations
"The developers", "Team 10", "we": The development team for the project, consisting of Jack Harris, Rory Kemp, Raul Sheth, Luke Tan, Nathan Hardcastle and Georgi Petkov.

"The client", "Microsoft": The client for this project, consisting primarily of Lilia Georgieva, but including Microsoft as a whole.

"The users", "the applicants", "the candidates": The people who will be solving the puzzles in this system and participating in the rankings. In other words, the people the client will want to consider as potential applicants for graduate software roles.

### 1.4 References
[UML Use Case Diagrams]

### 1.5 Document Overview
Describe what the rest of the document contains and how it is organized.

## 2. Product Overview
> This section should describe the general factors that affect the product and its requirements. This section does not state specific requirements. Instead, it provides a background for those requirements, which are defined in detail in Section 3, and makes them easier to understand.

### 2.1 Product Perspective
This product is being produced as part of the 2024 Group Design Practicals done by students in their second year of a Computer Science course at the University of Oxford. It emulates the interview process of most software companies, wherein candidates are asked a number of technical questions and puzzles in order for the interviewer to assess the ability of the candidate. The product shall be completely standalone, and not be part of any wider project.

### 2.2 Product Functions
The product shall:
* Provide a series of puzzles to the user for them to complete
* Provide a place for users to upload their code for their answers

* Provide a series of metrics from which the users' performance can be assessed
* Provide an overall ranking of the users

* Provide a login/accounts system for the users, so their progress can be kept between sessions
* Provide gamified elements within the puzzle to provide extra rewards to users and motivate them to keep trying the puzzles.


### 2.3 Product Constraints
The product will have the following constraints:
* The product will have to run in the web browser.
* The product will have to have its backend running on a lightweight server.
* The product will have to be developed within 2 months.
* The product will have to be GDPR-compliant.
* The product will be developed by six second-year undergraduates. 

### 2.4 User Characteristics
Identify the various user classes that you anticipate will use this product. User classes may be differentiated based on frequency of use, subset of product functions used, technical expertise, security or privilege levels, educational level, or experience. Describe the pertinent characteristics of each user class. Certain requirements may pertain only to certain user classes. Distinguish the most important user classes for this product from those who are less important to satisfy.

**User Class 1: Candidates**
These users will primarily be computer science graduates. They will be proficient in algorithmic thinking, and will have enough capability in a programming language to be able to produce computer programs that allow them to answer the puzzles. 

**User Class 2: Employers**
These will primarily be recruiters at Microsoft looking for hidden talent. They will be very proficient in algorithmic thinking and will have some degree of experience within the software industry. They will be able to assess the quality of the code of applicants.

### 2.5 Assumptions and Dependencies
The following assumptions are present:
* Candidates will have access to the internet and a web browser
* The metrics specified in this document will be useful in assessing the ability of users.

Since we will be making most of this from scratch, there are very few external assumptions about the operation of other software components.


### 2.6 Apportioning of Requirements
Apportion the software requirements to software elements. For requirements that will require implementation over multiple software elements, or when allocation to a software element is initially undefined, this should be so stated. A cross reference table by function and software element should be used to summarize the apportioning.

| Requirement | Software Element | 
| ----------- | ---------------- | 
|             |                  |           
|             |                  | 
|             |                  |           



Identify requirements that may be delayed until future versions of the system (e.g., blocks and/or increments).

## 3. Requirements
> This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

> The specific requirements should:
* Be uniquely identifiable.
* State the subject of the requirement (e.g., system, software, etc.) and what shall be done.
* Optionally state the conditions and constraints, if any.
* Describe every input (stimulus) into the software system, every output (response) from the software system, and all functions performed by the software system in response to an input or in support of an output.
* Be verifiable (e.g., the requirement realization can be proven to the customer's satisfaction)
* Conform to agreed upon syntax, keywords, and terms.

**Requirement Template**

**Requirement Name**:

**Requirement Number**: 

**Requirement Type**: 

**Use Cases**:

**Description**:

**Rationale**:

**Fit Criterion**:

**Priority**:

**Conflicts**:

**Dependencies**:

### 3.1 External Interfaces
> This subsection defines all the inputs into and outputs requirements of the software system. Each interface defined may include the following content:
* Name of item
* Source of input or destination of output
* Valid range, accuracy, and/or tolerance
* Units of measure
* Timing
* Relationships to other inputs/outputs
* Screen formats/organization
* Window formats/organization
* Data formats
* Command formats
* End messages

#### 3.1.1 User interfaces
Define the software components for which a user interface is needed. Describe the logical characteristics of each interface between the software product and the users. This may include sample screen images, any GUI standards or product family style guides that are to be followed, screen layout constraints, standard buttons and functions (e.g., help) that will appear on every screen, keyboard shortcuts, error message display standards, and so on. Details of the user interface design should be documented in a separate user interface specification.

Could be further divided into Usability and Convenience requirements.
________________________________________
**Requirement Name**: Login Screen

**Requirement Number**: 1

**Requirement Type**: User Interface - Functional

**Use Cases**: Used when candidate wants to log in and start/continue solving the puzzles.

**Description**: A login screen, where a user can enter their details and "log in", allowing them to continue the puzzle they are currently working on with their progress saved.

**Rationale**: If we are implementing an accounts system then there should be a way to log in to your acount.

**Fit Criterion**: A test user can enter their details and log in, and then be taken to the main part of the system.

**Priority**: Should have

**Conflicts**: None

**Dependencies**: Accounts System
________________________________________
**Requirement Name**: Puzzles Screen

**Requirement Number**: 2

**Requirement Type**: User Interface - Functional

**Use Cases**: User is solving puzzles/ submitting solutions

**Description**: There will be a portion of the screen displaying the current puzzle, alongside another part of the screen where the answer to the puzzle should be entered. There will also be an area where the user can submit their code for that puzzle.

**Rationale**: The user needs tio be able to view the puzzle, and be able to submit their answer and their code

**Fit Criterion**: A test user can view a puzzle and submit a solution alongside their code.

**Priority**: Must have

**Conflicts**: None

**Dependencies**: Partial dependency on account system
_________________________________________
**Requirement Name**: Progress Bar

**Requirement Number**: 3

**Requirement Type**: User Interface - Functional - Gamified Element

**Use Cases**: The user wants to see how far they are through the puzzles

**Description**: A progress bar that shows the user how many puzzles they have solved and how many more they have to solve

**Rationale**: A progress bar would fall under one of our gamified elements - seeing it will motivate our users and make them feel like they're making progress. Seeing the bar go up will be a kind of reward.

**Fit Criterion**: There is a progress bar that increases when a test user goes through the puzzles

**Priority**: Could have

**Conflicts**: None

**Dependencies**: Account System, Puzzle System, Puzzles Screen
_______________________________________________
**Requirement Name**: Trophy Area

**Requirement Number**: 4

**Requirement Type**: User Interface - Functional

**Use Cases**: A user wants to see which trophies they have earned.

**Description**: A sidebar that the user can enter to see which trophies they have earned.

**Rationale**: When awarding the user trophies and other similar gamified elements, a huge part of why that is engaging is the user's ability to view their trophies. If this is not implemented, the users will not have a way of reflecting on their achievements.

**Fit Criterion**: A test user can click on the sidebar and view their trophies.

**Priority**: Could have

**Conflicts**: None

**Dependencies**: Trophy System, Puzzle System, Puzzles Screen
_________________________________________________
**Requirement Name**: Metrics Interface

**Requirement Number**: 5

**Requirement Type**: User Interface - Functional

**Use Cases**: The employer wants to view a user's metrics, or the overall rankings of users

**Description**: An area solely for the employer where they can view user metrics and the overall rankings of viewers. It should be easy to view the top 10% of users in particular. These metrics will include the time taken for each question and the ability to view a user's code for each puzzle they have solved.

**Rationale**: We want the client to be able to view the data on the users, otherwise this whole system does not fulfill its purpose of enabling the client to find technical talent.

**Fit Criterion**: A test user can view the metrics of other candidates. This data should be verified to be correct by another test user logged into the candidate accounts.

**Priority**: Must have

**Conflicts**:None

**Dependencies**: Accounts system, Puzzles system
_________________________________




#### 3.1.2 Hardware interfaces
_______________________________
**Requirement Name**: Website Implementation

**Requirement Number**: 6

**Requirement Type**: Hardware Interface - Functional

**Use Cases**: The user wants to access our website

**Description**: The system should be implemented so a web browser can interact with it

**Rationale**: We want this system to be as easy to access as possible, and so a website is the natural choice.

**Fit Criterion**: A test user can view the website using their web browser.

**Priority**: Must have

**Conflicts**: None

**Dependencies**: None
_______________________________


#### 3.1.3 Software interfaces
____________________
**Requirement Name**: Database Interface

**Requirement Number**: 7

**Requirement Type**: Software interface - Functional

**Use Cases**: Within the account system

**Description**: The system must interface with a database to store user data

**Rationale**: In order to have an ordered way of storing this information, it would be best to have a database with all this information on it. In order to do this, we must have some way of interfacing with the database management system.

**Fit Criterion**: Database features work

**Priority**: Should have

**Conflicts**: None

**Dependencies**: None
___________________

### 3.2 Functional
___________________________
**Requirement Name**: Puzzle System

**Requirement Number**: 8

**Requirement Type**: Functional

**Use Cases**: Answering or viewing puzzles

**Description**: A system that allows users to view puzzles and submit answers for them. If the answer to the puzzle is wrong, the system should not allow the user to proceed. If the answer is correct, the user should be provided the next puzzle.

**Rationale**: We want the users to be able to view and answer the puzzles, so we need to build that functionality.

**Fit Criterion**: A test user can view and answer the puzzles.

**Priority**: Must have

**Conflicts**: None

**Dependencies**: Website implementation. Partial dependency on Accounts System.
____________________________
**Requirement Name**: Accounts System

**Requirement Number**: 9

**Requirement Type**: Functional

**Use Cases**: The user wants to track their progress between visits to the site. The employer wants to view a user's data.

**Description**: A system that interacts with a database to store user data. This should include username, password and email, alongside progress through the puzzles and any unlocked trophies.

**Rationale**: We want to keep track of the user data to allow the client to assess their ability. This necessitates a system that stores and manages all this data.

**Fit Criterion**: Test users can retain their progress between sessions if they have completed any puzzles, and other test users can view this progress.

**Priority**: Should have

**Conflicts**: None

**Dependencies**: Database interface, Puzzle system
___________________________

**Requirement Name**: Trophy System

**Requirement Number**: 10

**Requirement Type**: Functional - Gamified Element

**Use Cases**: A user achieves something noteworthy and should be rewarded

**Description**: A system that awards "trophies" to users to reward them for doing something noteworthy. It should keep track of which trophies each user has, and detect when it should award them new trophies.

**Rationale**: This is the main gamified element of the overall system, and we want these gamified elements to motivate players to keep trying at the puzzles. Giving them bonus rewards further incentivises them to keep trying their hardest, and also provides more metrics for the employer to differentiate candidates by.

**Fit Criterion**: A test user should unlock trophies for completing certain tasks.

**Priority**: Could have

**Conflicts**: None

**Dependencies**: Accounts System
____________________________________

### 3.3 Quality of Service
> This section states additional, quality-related property requirements that the functional effects of the software should present.

#### 3.3.1 Security
_____________________________
**Requirement Name**: Password Encryption

**Requirement Number**: 11

**Requirement Type**: Non-functional

**Use Cases**: Whenever a user has a password

**Description**: A system that ensures passwords are not stored in plaintext and are transmitted thoroughly

**Rationale**: We want our users' passwords to be safe and secure. 

**Fit Criterion**: Passwords should not be stored or transmitted in plaintext

**Priority**: Should have

**Conflicts**: None

**Dependencies**: Account System

### 3.2 Compliance
__________________________
**Requirement Name**: GDPR Compliance

**Requirement Number**: 12

**Requirement Type**: Non-Functional - Legal

**Use Cases**: Whenever user data is stored

**Description**: Our accounts and database systems should be GDPR-compliant.

**Rationale**: This is a legal requirement.

**Fit Criterion**: All requirements given by GDPR are met.

**Priority**: Must have

**Conflicts**: None

**Dependencies**: Accounts System, Password Encryption
_________________________

### 3.5 Design and Implementation

#### 3.5.1 Installation
Constraints to ensure that the software-to-be will run smoothly on the target implementation platform.

#### 3.5.2 Distribution
Constraints on software components to fit the geographically distributed structure of the host organization, the distribution of data to be processed, or the distribution of devices to be controlled.

#### 3.5.3 Maintainability
Specify attributes of software that relate to the ease of maintenance of the software itself. These may include requirements for certain modularity, interfaces, or complexity limitation. Requirements should not be placed here just because they are thought to be good design practices.

#### 3.5.4 Reusability
<!-- TODO: come up with a description -->

#### 3.5.5 Portability
Specify attributes of software that relate to the ease of porting the software to other host machines and/or operating systems.

#### 3.5.6 Cost
Specify monetary cost of the software product.

#### 3.5.7 Deadline
Specify schedule for delivery of the software product.

#### 3.5.8 Proof of Concept
<!-- TODO: come up with a description -->

## 4. Verification
> This section provides the verification approaches and methods planned to qualify the software. The information items for verification are recommended to be given in a parallel manner with the requirement items in Section 3. The purpose of the verification process is to provide objective evidence that a system or system element fulfills its specified requirements and characteristics.

<!-- TODO: give more guidance, similar to section 3 -->
<!-- ieee 15288:2015 -->

## 5. Appendixes
