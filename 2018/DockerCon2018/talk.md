# DockerCon 2018 - "Lessons Learned Running Docker at Extreme Scale"
## Author: Angel Rivera

## Abstract
The ascendance of Docker has helped bring about about a new focus on some software development values that are dear to our heart at CircleCI—consistency, automation, and continuity; that is, developing software within a consistent build environment, testing it in an automated fashion, and deploying it with a focus on continuous delivery of new code.

We released CircleCI 2.0 with these values in mind, placing Docker at the core of our Continuous Integration platform and allowing customers to build projects on CircleCI using any combination of Docker images as build environments.

CircleCI’s images for popular languages + frameworks have over 38M+ pulls on DockerHub. Docker images are an incredible asset for ensuring that your dev and production environments are mirrors. But, with every new technology comes added complexity and management overhead.

In this session, CircleCI CTO Rob Zuber will share some lessons learned in running Docker at scale, across thousands of customers, their language + technology choices, and their environments. With over 350,000 users and 10M+ jobs per month, we’ve seen up close how customers can succeed with Docker, and how to avoid potential issues.

## Talk Outline
- My Introduction
    - Introduce yourself
- Agenda
    - Set Presentation Expectations 
- Brief history of v1.0 tech stack
    - How did it used to be?
- Intro into 2.0
    - What changed from 1.0
- Why Docker?
    - Decision factors
- Lessons Learned
    - Bad parts
    - Good parts
- Demo
    - Live code Python App
    - Live code python unittest
    - Live code v2.0 CircleCI config
        - add ssh keys
        - run tests
        - Wire up a deploy to Digital Ocean Server via Docker
    - Push "broken: code to repo cause build failure
        - Fix code
    - Push Fixed Code to repo
    - Show CircleCI build go Green
    - Have Audience go to hello.dpunks.org to see the app
    - End of Demos\Questions

## Talk Script

### Slide: My Introduction
Welcome everyone. Some of you are expecting Rob Zuber CircleCi's awesome CTO but unfortunately he is unable to present so I'll be subbing for him today and I'm really EXCITED to be speaking to all of you.

So my name is Angel Rivera & I'm a Developer Advocate for CircleCI. As a Developer Advocate my job is to directly engage developers... & you the community. 
Before we begin I want you all to know that this is my 1st conference talk as a CircleCI Developer Advocate and I intend to make it memorable.

### Slide: hello.dpunks.org - Broken
Before I start coding I'd like to ask everyone to open a browser & go to `hello.dpunks.org` & tell me what you see.  Just yell it out....
The answer is nothing. This my broken "Production" server on Digital Ocean that doesn't have an app running on right now ut it will after this demo

### Slide: Demo
My presentation style is heavy on the demos & light on the slides so I'm show you how to quickly implement Continuous Integration Continuous Delivery CI\CD pipelines into your code base using Docker & CircleCI. In this demo I'm going to write a simple web app, some unit tests & implement a CI\CD pipeline that will deploy the app to a live Digital Ocean server. Sound Good!

### Demo: Live Code App & Unit Tests
Ok lets get started
- Write a python flask app
- Write unit tests

### Demo: Walk through the CircleCI Config
Now we can add a CI/CD pipeline to our code base.  For this demo of course I'm going to use CircleCI.
It's really simple to do.
- In the root of your project repo create a `.circleci` folder
- Within the `.circleci` folder create a config.yml file which is your CI/CD configuration file

This is very simple CI\CD pipeline configuration
- Jobs are XXXX
- Builds are XXXX
- Docker images provide more build flexibilty for users etc... TODO:
- Code Checkout from Github
- Add SSH Keys that enable access to our target server
- Install app dependencies
- Run the unit tests that I wrote earlier
- Run PyInstaller to package my app into a single binary with all it's dependencies
- Finally we push the binary package to the production server then kickoff a deployment script sitting on the server which initializes and runs the app inside a docker container

### Demo: Kick off Build process - Failure
We have our 3 components the app, unit test & the ci/cd config file.  Now it's time to kick off the build.  If all goes well we should see the Hello DockerCon message on the server.

The CircleCI platform is watching this repo for changes like commits or pull requests & will run any config.yml files it finds so I'll commit this code to kick off our build.

- kick off the CircleCI build `git commit`

**Build will fail Intentionally - Missing Exclamation Point**

### Demo: Kick off Build process - FIXED
The build failed and it looks like I wrote some bad code. Right so it looks like I forgot to the exclamation point in my Message string. So lets fix that & try again.

- Add `!` to the message string
- kick off build again `git commit`

Success

### Slide: hello.dpunks.org
Audience: In a browser got to `hello.dpunks.org` Cool we've successfully implemented a CI/CD pipeline & using automation deployed our app to a production server. The app is running in a docker container on a single Digital Ocean server but this pipeline can be extended to also deploy to other hosting platforms such Kubernetes or DC/OS clusters.

### CircleCI 2.0
 CircleCI Version 2.0 leverages Docker

### Slide: CircleCI Stats
CircleCI processes:
- 12 Million+ builds per month
- 500K+ builds avg per WeekDay
- 11.3M Projects

Our users are crushing it in regards to CI\CD.  Lots of quality code being written.

## Tech Stacks
Here is a list of tech stacks being used:
- python 2.7.14
- unittests
- flask
- pyinstaller
- virtualenv
- docker
- CircleCI configuration
- Digital Ocean server



# Misc Notes & Scratch Pad

#### Slide: What is CircleCI
CircleCI is a Continuos Integration Continuos Delivery\Deployment platform that enables developers to rapidly release quality code by automating the build, test, and delivery process.

Quick show of hands how many of you are familiar with CI\CD?


### Slide: CircleCI Version 1.0 - Pre Docker
Version 1 of the platform was launched in 2011 before the Containerization Boom so it executes builds on dedicated VMs using a selection of Ubuntu Linux and for mobile builds Ubuntu w/ Android SDK & OSX for XCode code bases. v1.0 is an awesome innovation but as our business processes evolve & new technologies emerge so must our platform. As usage increased customers required flexibility in their pipelines.

### Slides: CircleCI Version 2.0
CircleCI addressed their customers needs in the form of v.20. I wasn't with the company during the v2.0 design but the team shared early v2.0 internal docs with me which illustrated their design & technology considerations. The teams thoroughly debated decisions such as whether or not to roll their own stack vs incorporating existing off the shelf solutions where appropriate. A topic that stood out to me was around choosing a containerization stack for the 