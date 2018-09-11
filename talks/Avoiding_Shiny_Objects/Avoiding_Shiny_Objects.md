# Apps, Stacks, and Frameworks: Avoiding “Shiny Object” Syndrome

## Author: Angel Rivera

## Abstract

DevOps teams are in constant search for magical solutions to their technology woes, but not properly vetting solutions can cause unintended effects. These choices lead to bad design/architecture decisions & compound technical debt. In this talk, I’ll share advice to avoid the Shiny Object syndrome.

## Description

Technology is fast moving, and devops tools pop up like wildfire. Teams are desperate to solve their problems & often make implementation decisions based on word of mouth, “kick the tires” syndrome or superficial evaluations. In some cases we justify our stack decisions based on project/sprint deadlines, the product’s marketing materials, occasionally, the README files. Really scary stuff!
In this talk I’ll explore how & why teams are easily lulled into believing that shiny objects will independently solve their stack deficiencies. I’ll discuss my experiences with “Shiny Object” frameworks/tools and the true impact they had in actually solving problems. I’ll also discuss some strategies that can help teams make better choices when properly vetting potential solutions based on my experience in the federal government evaluating vendor proposals and homegrown solutions, as the sole DevOps engineer at a startup, and now from my experience at CircleCI.

## Talk Outline

The overall idea here is to discuss my observations of tech teams, they're approaches to change and offer my thoughts on improving.

### Intro

`Define shiny objects for the audience` Immediate solutions to problems or an all in one solution

`Story`:

I want to open with a story.

A development team is assigned a new project to add new features to a Web UI
The stack is critically dependant on MySQL for persistence and the team quickly realizes their current relational data model is going to be a big problem in implementing the new features.

The new features required a hierarchical data model with deep nesting which is the opposite to their flat data model. The team was deeply frustrated with their data model constraints but a developer offered a solution. This developer was experimenting with an open source project called MongoDB which supported hierarchal data models. MongoDB was billed as a "Schema Less" data store and that concept was very appealing to the team because they assumed it could future proof data models.

The developer quickly built a prototype of the new Web UI features using MongoDB to store the data. The developer proved that MongoDB solved their data structure issues. The team was relieved and decided on implementing the MongoDB solution. They estimated it would take a few more days to finish prototyping and have a stable release of the new features.

The team recognized that implementing MongoDB would add a new dependency to the stack along with supporting new infrastructure. MongoDB presented a problem for the ops team because nobody had any operational experience with the platform. The developer was the only person with MongoDB experience so the ops team relied on his knowledge to deploy the new infrastructure. The dev team built a stable release and ops deployed the new Web UI features into production.

The project goals and deadlines were met and customers were extremely happy with the new features.

The End...

`Ask the audience` to identify the shiny object(s)

- MongoDB
- "Schema Less" promise to future proof against Schema incompatibilities

`Break down the main points` of the story

- Driving the change New Web UI Features based on customer demands
- Flat Relational vs Hierarchical Schemas
- Schema Less data models
- 

Not Quite



Fast Forward T+ 90 days


 
 `Slide Idea` show a Flat Table & Json  

I developer on the team suggests that 

They brainstorm

Brainstorming:
  - Why did you pick this topic?
    - Talk about desperate teams, describe them how are they lulled?
      - What is a desperate team?
        - Teams that hehehe
    - Talk about your experience with shiny object syndrome. Successes/Fails 
      - Talk about impact of success/fail. What are the results
    - Advice on team cultures
  - What do you want to share?
    - Reasons to adopt new technologies Why do it?
    - Stories about and Impact of choices related to adopting new tech Pros/Cons
    - Thoughts on how to adopt new tech
  - 

### One: Team Profiles

- Profiling Teams. Discuss general characteristics Pros/Cons
- Innovative: Focus on creating/improving
  - `Define:` 
- Proactive: Focus on maintaining/preventing issues, future proofing
  - `Define:` 
- Reactive: Focus on resolving issues
  - `Define:` 
- Compare all characteristics
  - Map characteristics to Real-world examples (Pros/Cons) use a table Char, Focus, Best Fit Scenario

  | Char | Focus | Best Fit Scenario |
  | ------ | ------- | ----- |
  | Innovative | Creating/Improving | Design and implement new features,  |
  | Proactive | Maintaining/Preventing | Monitoring/Analyzing performance, Mitigate potential issues |  
  | Reactive | Troubleshooting/Resolving | Rapidly Resolve Critical Real-time Outages, Skilled Troubleshooters |

- Converging Factor Change
  - Embrace/Implement Change
    - Modify an existing API service to support new GraphQL functionality
    - Update a MongoDB cluster to newer version predicting performance gains
    - Rewriting code to handle a changed key in a JSON dataset from an Integrated third party service
  - 

### Two: Vetting Practices

- Talk about various team vetting practices
  - Which teams tend to do what
- Give examples that correlate to each team profile & show impact of absent disciplines
- Show benefits of leveraged profiles
- Which characteristics should teams strive for?)
  - Teams should strive to have all three characteristics and ability to leverage them disproportionately
- Correlate success/failure to culture/people

Topic: Stories about and Impact of choices related to adopting new tech Pros/Cons

Brainstorming:

- Stories relevant to the reasons above
- Talk about classifying team behaviors:
  - SF Chillaxed
    - Work fast and loose
    - Stays current
  - Suits/Enterprise/Gov
    - Disciplined 
    - comes at a cost

### Three: - Advice Bettering culture

- Leader/Managers
  - Flat management structure
    - Define SUDO rule, set expectations
    - Facilitates Individual Equality
    - Lead by example
  - Emphasize Learning
    - Inspire teammates to learn new things
    - Encourage pursuit of interests
    - Provide time/resources to learn
- Lead Individuals
  - Commit to learning
  - Be open to ideas
  - Do the work 
  - Transparency

### Outro

## Talk/Slides Script

1. Title Slide: Apps, Stacks, and Frameworks: Avoiding “Shiny Object” Syndrome
2. Bio Slide: 
3. I'm going ot set expectations here. This Talk is not about technology
4. I'm going to talk about my experience with tech teams and how we vetted technology.
5. In order to do this I'm going to have to do some profiling and categorized types of teams I've experienced.
6. I’ve classified team into the following categories: Innovative, Proactive, Reactive and I'll describe each
7. Innovative: title slide nothing to say here
8. Innovative teams are focused on creating and improving, they deal in the New Hotness. Like designing and implementing new features or services.
9. Proactive: title slide no text
10. Proactive teams focus on maintenance and prevention. they deal in stability. Some examples of proactive behaviors are monitoring and analyzing performance in order to suss out unknown issues. They lean towards future proofing solutions.
11. Reactive: title slide to text
12. Reactive teams focus on troubleshooting and resolving. These are teams that rapidly resolve critical Real-time outages. they are very skilled troubleshooters.
13. Team Profile summary slide
14. All of these teams must manage and implement change though their approach may differ.
15. 
16. These teams converge on some common factors but I’m going to focus on one...
17. 

### Slide: Introduction


# Random Notes Section

- What are they?
  - I like the phrase "The new hotness" to describe shiny objects
  - Immediate solutions to problems
  - Some examples examples of shiny objects:
    - DevOps it's not software or cloud infrastructure that offers zero maintenance or management
    - REST APIs they won't directly improve inadequate services
    - Micro services don't provide out of the box scalability for your stack with minimal effort
  - Shiny objects are basically distractions in our quest for all in one solutions
- Developers are susceptible to shiny object syndrome because:
  - We are problem solvers
    - It's in our DNA
    - We want to resolve issues quickly then move onto the next issue
  - We want to cut complexity
    - Have less moving parts
    - Encapsulated functionality so everything is black boxed
    - Eliminate unnecessary code or infrastructure so we can run lean run lean
- The ultimate goal is to collapse everything in manageable bits
- To me, an "Easier" life means:
  - Reclaiming Time useless or redundant tasks
  - Enabling developers to work on projects that inspire them
  - Refocusing efforts on innovative initiatives
  - Reallocating Budgets invest on initiatives that matter
  - Meeting deadlines and target goals with minimum effort
  - Basically an awesome technology utopia
  - A Nerf Gun battle, D&D, Cosplay nirvana
  - Beautiful... Right?
- Reality: Ok now let's Pump the Breaks and focus on reality people
  - The reality is:
    - Software is very complicated
    - There are lots of moving parts
    - Black boxes are very helpful if they're well designed...
    - Unnecessary code is very difficult to purge
      - Raise your hand if you have ever eliminated code only to find that your change broke a critical service and you had to quickly reinstate that code to resolve the issue?
    - Legacy code is like cockroaches... very hard to get rid of
    - As developers:
      - We code new features, test code and fix bugs
      - We maintain inherited code
      - Adhere to aggressive release schedules
    - On the flip operators/SREs:
      - Architect infrastructures
      - Monitor and Maintain Infrastructures
      - Ensure system Integrity and Security of these infrastructures and all the while technology advances at light speed rendering our current changes outdated.

- We're automating and imitating real-world actions, conditions and objects using Zeros, Ones and electricity