# Build for Production using CI/CD Pipelines & Docker

## Author: Angel Rivera

## Abstract

The ascendance of Docker has helped bring about about a new focus on some software development values that are dear to our heart at CircleCI—consistency, automation, and continuity; that is, developing software within a consistent build environment, testing it in an automated fashion, and deploying it with a focus on continuous delivery of new code.

We released CircleCI 2.0 with these values in mind, placing Docker at the core of our Continuous Integration platform and allowing customers to build projects on CircleCI using any combination of Docker images as build environments.

CircleCI’s images for popular languages + services have over 38M+ pulls on DockerHub. Docker images are an incredible asset for ensuring that your dev and production environments are mirrors.

In this session, CircleCI Developer Advocate Angel Rivera will offer Docker & CircleCI to demonstrate how developers can easily integrate CI/CD pipelines into their projects and securely, build, test, release & deploy production ready Docker images.

## Talk Script

### Slide: Introduction

- Welcome everyone! My is Angel Rivera & I'm a Developer Advocate for CircleCI.
- Today I'll be discussing CI/CD Pipelines & Docker

### Slide: CircleCI (Logo)

- Quick show of hands who uses CircleCI?
- For those wof you who don't know, CircleCI is a Continuos Integration Continuos Delivery/Deployment platform that provides rapid release of quality code by automating the build, test, and delivery process.
- Quality code delivered consistently and faster

### Slide: CircleCI Stats

CircleCI processes:

- 12 Million+ builds per month
- 500K+ builds avg per WeekDay
- 11.3M Projects
- Our users are crushing it in regards to CI\CD. Lots of quality code being written.

### Slide: CircleCI + Docker

- Some of those stats can be attributed to the technologies that we integrated into the platform.
- CircleCI v2.0 relies on Docker for most project builds. 
- Docker gives our users the flexibility they require & enables them to test in environments almost identical to their operational infrastructures.

### Slide: “But it worked on my box”

- Raise your hands if you've ever heard or uttered this phrase
- Apps work on developers box but not in qa staging or production

### Slide: Why? `¯\_(ツ)_/¯`

- Who knows why this happens?
- Developers & Ops staring at each other that high-noon blame posture

### Slide: Inconsistent App Environments

- In my experience the root cause was Inconsistent Application Environments
- Developer systems may have missing or older app dependencies
- Developers local Operating systems are different than target environments
- There numerous reasons for the disparity in our environments...

### Slide: How can we equalize?

- How can we level the playing field in our environments?

### Slide: Docker (Logo)

- CircleCI leverages Docker images to eliminate these issues for our users.
- Docker Images enable developers to mint application environments which gets them as close as possible to their target environments whether it be development or production.

### Slide: Equalizes App Environments

- Using docker teams can consistently spawn & run applications regardless of the target infrastructure.

### Slide: Demo (Diagram)

It’s demo time!

- Now I’m going to show you how to quickly implement Continuous Integration & Continuous Deployment CI\CD pipelines into your code base using Docker & CircleCI.

In this demo I'm going to:

- write a simple web app and a unit test
- implement a CircleCI configuration that will build, test, generate a Docker image & publish it to Docker Hub
- Finally, the application will be running in a Docker container on a live Digital Ocean server.

### Slide: Code!

Start Live Demo here

### Demo: Live Code App & Unit Tests

Ok lets get started

- Write a python flask app
- Write unit tests - make test fail here
- Explain the builds are executed by git push to upstream repos
- Show CircleCI Dashboard & the build fail
- Fix the typo in the app, git commit /push the fix then show the build restart

### Demo: Walk through the CircleCI Config

Now while the fix is building walk through the config file

- In the root of your project repo create a `.circleci` folder
- Within the `.circleci` folder create a config.yml file which is your CI/CD configuration file

This is very simple CI\CD pipeline configuration

- Jobs are XXXX
- Builds are XXXX
- Docker images provide more build flexibilty for users etc... TODO:
- Code Checkout from Github
- Install app dependencies
- Run the unit tests that I wrote earlier
- Run PyInstaller to package my app into a single binary with all it's dependencies
- `Setup Remote Docker`: spins up new linked container with docker client installed & enables docker builds.
- Build Docker image based off of the project DockerFile
- Docker Hub login creds are securely saved in the CircleCI platform & referenced in config using Environment Variables
- Docker push the build to Docker Hub
- Finally a deployment build is kicked off on the Digital Ocean server that docker pulls & runs as a container

### Demo: CircleCI Dashboard - Fixed Build

- Show the Fixed build component
- Show the Tests
- Show the Docker Hub Build & Push logs

### Slide: hello.dpunks.org

Audience: In a browser go to `hello.dpunks.org` Cool we've successfully implemented a CI/CD pipeline & using automation deployed our app to a production server. The app is running in a docker container on a single Digital Ocean server but this pipeline can be extended to also deploy to other hosting platforms such Kubernetes or DC/OS clusters.

### Slide: Lessons Learned

- I wanted share some our Docker Lessons Learned
- Some users are new to Docker so they’re exposure is minimal.
- CircleCI has a huge investment in self serve educational content as well as a top notch support team
- Some users deploy their Docker “Test” images to production which is def a something you don’t want to do.  
- Production images should be lean & only include required dependencies. Running test images in production can lead to performance issues since the images are bloated and can have performance hindering debug tools installed.

### Slide: Thank You

- Thank you for attending! You can reach me via twitter or come over to the CircleCI Booth if you'd like to discuss CircleCI or any other topics.

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
