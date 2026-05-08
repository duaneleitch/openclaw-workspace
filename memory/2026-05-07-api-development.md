# Session: 2026-05-07 23:01:29 UTC

- **Session Key**: agent:main:discord:channel:1478436599074258954
- **Session ID**: 98cafc18-aa39-49dd-afc4-c8db95da3939
- **Source**: discord

## Conversation Summary

assistant: Done.

Created:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-15 Internal ABCRC Integration and Data Synchronization Strategy Meeting.md`

Send the next one.
user: Continue the OpenClaw runtime event.
assistant: Ready. Send the next transcript.
user: [media attached: /home/duane/.openclaw/media/inbound/2026-04-15_Dav_Duane_Data_Integration_API_Development_and_Pr---cbd435fb-cabe-49c2-9e1a-a29527a5ad02.md (text/markdown) | /home/duane/.openclaw/media/inbound/2026-04-15_Dav_Duane_Data_Integration_API_Development_and_Pr---cbd435fb-cabe-49c2-9e1a-a29527a5ad02.md]
[Discord #alfred-main channel id:1478436599074258954 +2m Thu 2026-05-07 13:26 UTC] Leitchy (dl_70): <media:document> (1 file)

<file name="2026-04-15_Dav_Duane_Data_Integration_API_Development_and_Pr---cbd435fb-cabe-49c2-9e1a-a29527a5ad02.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="42fc0c173dbb734e">>>
Source: External
---
# 2026-04-15 Dav:Duane Data Integration, API Development, and Project Management Discussion
Creation Time: 2026/04/15 11:29


## Transcription

**00:00:00 - 00:00:20**
Good morning, Dav. Good morning. How are you today? Getting a little bit apprehensive. Oh, yeah? Why? We have a yellow storm warning in effect. We can get up to actually about 25 centimeters of snow in the next 24 hours. Wow.

**00:00:22 - 00:00:34**
So I'm going to let you know in advance that my computer is doing something weird, so my screen keeps going. Blank, so if I lose you, I'll join on another computer. I'm not sure what's going on.

**00:00:35 - 00:00:37**
That's because you live in an earthquake zone.

**00:00:38 - 00:00:44**
I know, right? It was 4.0 on the Richter. Oh, wow. Yeah, yeah.

**00:00:44 - 00:00:46**
And whereabouts are you in Ontario?

**00:00:46 - 00:00:53**
So I'm just west of Ottawa. I would say about an hour west of Ottawa.

**00:00:55 - 00:00:56**
You're not even in the GTA.

**00:00:57 - 00:01:04**
Nope, nope. I'm about four hours from where Roger and them are at.

**00:01:06 - 00:01:11**
Oh, okay. So diverse main office is in the GTA, right?

**00:01:11 - 00:01:11**
Correct, yeah.

**00:01:12 - 00:01:17**
Yeah. So you work remotely all the time too?

**00:01:18 - 00:01:20**
Correct, yeah. Yeah, the whole team does actually.

**00:01:22 - 00:01:22**
Ah.

**00:01:24 - 00:01:48**
So speaking. Of the team, I don't know if you saw my update. Um, but in regards to and we're going to use the term the ASR, it was identified way back in 2024 that Diverse had to accept the extrapolation data from that.

**00:01:48 - 00:02:33**
Yeah, I did see your update, so. I don't think they're arguing that this is a new requirement. So, so I think that's okay. Yeah. Yeah. I don't, I would be very surprised if they came back and said, you know, this is a brand new requirement and you guys just dropped this on us. So no, I don't think that's it. I think it's more of a technology question. And I think that's where Mark was coming from was like, you're already producing the ASR. So does it make sense for us to move it? And you know, if, if we are to do it, are we able to, to do it? Because it's a, it's these. A couple additional fields that don't fit into the framework and that kind of conversation. Right, right. Sorry, go ahead. Go ahead. No, after you.

**00:02:36 - 00:02:38**
We're back and forth. We're being too kind. Go ahead.

**00:02:40 - 00:03:35**
I think we got caught up on the word report. Yeah. And we just focused on that little printout, not the fact that the ASR is actually an updated R bill. And I think that's really what happened over the last year. We just got into this cycle of thinking it was a piece of paper that we sent out, and in reality, that's a side thing, and it's not the actual ASR. Yeah, I agree. So I met with the team urgently yesterday afternoon. And so, yeah, so those six items I sent you were critical items. Uh, the four items that were left from the ten were just basically cosmetic stuff and going, guys, that's, that's not critical. Who really cares? Yeah, okay, but uh, yeah, so I did, uh. After that meeting, I spent some time with Salmon Chain.

**00:03:35 - 00:03:49**
So we have contractual obligations, uh, that we have to meet in, um, a volume, uh issue, so yeah, um. It's a pretty important item.

**00:03:49 - 00:04:38**
Yeah, so what I did was I took the information that you provided me, so I basically chunked it into three categories because that's kind of where it falls. So the three categories, and I captured all your information, by the way. One was the NAB data integration, so the R bill must be able to accept and populate extrapolation data from NAB. So that means that information needs to be in diverses. Sorry, my screen just went blank. Um, the second one was about the locking. Uh, so QC State must stay editable, so that's the air bill. Uh, selected, blah, blah claims. Ready? You still need to be able to edit it, and then the uh, uh. So the editability and the controlled locking are kind of the same. Follow for kind of in the same thread.

**00:04:38 - 00:05:27**
But I chunked it out as the third item, so basically, I condensed all of what you provided into those three categories. And, uh. Essentially, just as we were saying, it kind of boils down to one common thread, and it's that your requirement is that Diversys accepts and stores and is able to use the extrapolation data from NAV. And however you choose to use that, whether it's for an ASR report or whatever, it doesn't matter. It needs to be in the system. Right. Yeah, so that's my position that I'm going into the meeting today with. And so, you know, to be completely transparent, as you know I am, I told them that we need to make, there's two major decisions. One is, can we do it? Like, so technically, can we do it?

**00:05:27 - 00:06:03**
If we can't, then we need to talk about that and figure out what our options are. Two is, if we can do it, then we need to make a decision, a business decision. Are we going to do it? Right, if the answer is yes, then fine, we, we can. We can come back to you guys and say, you know, we're going to do that stuff, and you know, here's then you and I can talk about how it fits into the project plan, etc. If the answer is no, then then we're going to have some difficult conversations and and we'll have to see where it goes from there. So I don't know those those answers to those questions yet, but my meeting's at four o'clock, so I'll of course, update you.

**00:06:05 - 00:06:42**
It might not be today, but I will get back to you with what the position is. And then you and I will figure out the plan. My expectation, to be honest, is that we're going to do it, right? We're in a partnership with you guys. We're going to do it. And then you and I need to figure out the timing and the impacts to the schedule. When we do it. And as you said, even though it came up a year ago, I I think it's kind of irrelevant. And I don't mean to like, say that it's not important, it's I'm saying, it's irrelevant that it came up a year ago. Because the integration needs to be got be done in order to use it anyway. So they probably would have held held off on actually developing it till now anyway.

**00:06:42 - 00:07:07**
Right, right, right, and I, So, yeah, the the NAV communication pieces. Right. We take it on our shoulders that, wait a minute, we held off on that, okay, on the nav integration. Now, I was supposed to get actually a statement of work back from the guys. I'm going to reach out to them again today.

**00:07:07 - 00:07:08**
I was going to ask for an update.

**00:07:09 - 00:08:14**
Yeah. But we are engaging them, So we're going to be setting up a technical meeting with Mark and that, so that – everybody understands. Um, so when I first engaged them, I sent them the first API Uh document, and then when I had my meeting with them face to face, I gave them the updated. The the other, the better document. That really clarified things for me. And yeah, so they have that, uh, in the initial meeting, as they quickly went through it. It doesn't seem to be much surprising to them. So I don't think, well, I've got to wait until the statement of work comes back. So the first statement of work is simply for the solution design, okay? And then they'll give us a costing of the rest of it, development, testing, implementation, and whatnot.

**00:08:18 - 00:08:32**
And that led down another path, okay? So the list of APIs, that is a phenomenal amount of APIs, okay? The endpoints.

**00:08:32 - 00:08:34**
Yep. Yep, there's a lot.

**00:08:34 - 00:08:52**
Okay. So we did a high-level estimation on the cost of developing all those APIs, and we're looking at, An 800, 000 bill, yeah.

**00:08:52 - 00:09:35**
And so that, that's my point, is that you don't need to develop. It's not a one for one because we have an API endpoint, doesn't mean you need an API, that one API for each API endpoint, it's not a one for one matter. All roads lead to use cases, so what is your use case? And for that use case? It's like, I need to update our bill with these two fields. Okay, great, that's a use case. So what information needs to go from NAV back to Diversys, right? So it's a post. And so that would be a use case, right? This is the use case. This is what we need to do. This is why. These are the fields that need to be pushed back into Diversys and how that's triggered and all that.

**00:09:35 - 00:10:12**
So it comes down to use cases. So if you say. There's going to be function calls, so it's going to be a post. It's going to be a get. It's going to be maybe even a delete or an update. So whatever you guys need to do, you need to create use cases for that. And then they develop an API that says, okay, this is how that API is triggered. This is how it calls diverses. This is what it does once it's made the call to diverses. And this is what it pulls or this is what it gets back, so on. And then it's how do we take that payload and put it into now. So that's the. The formatting piece, and and that's what they were developing.

**00:10:12 - 00:10:15**
That's not where I was going, that's not where I was going away.

**00:10:15 - 00:10:16**
Okay, okay.

**00:10:16 - 00:10:18**
I skipped ahead.

**00:10:18 - 00:10:21**
Well, actually.

**00:10:21 - 00:11:24**
You went down the wrong river completely. The reason why I started saying that it was actually for this point here. I asked the question a few times, and the answer, Mark, and I believe you gave me, was no. And the question was actually for going into production, the initial load of configurable data. And I remember I used the example of like a simple Excel spreadsheet. If we have all that, can that be uploaded into Diverse to populate all the tables with our initial load of production data? And I think our depots are, don't quote me on this, I think there's 220 depots, right? And so the question was for the initial production, not ongoing, not ongoing at all, but for the initial production, how are we going to get all that data into the production system?

**00:11:24 - 00:12:34**
Um, was was the question, because when we looked at it, we realized that. On average, there may be one depot a year that needs an adjustment or to be added or to be archived. Like there's not a high turnover. So when we went through the API listings, we're going, well, we don't need to update the sites. And then we talked about the materials. Well, very seldom is there a change. Like, yeah, we're getting pallets in this year, but. That's something new, and there hasn't been anything new in 10 years, right? So, reviewing all those other APIS, we realized that the only one that is actually that we need is the one that we're trying to develop now. So then it was like, Well, how do we get the data into the production, not the training environment, but production environment? So do you guys have a viable solution that we can? Oh, you're showing me something.

**00:12:34 - 00:13:14**
Yeah, yeah, so this is kind of what I was talking about yesterday when, uh, when, uh, Andre was talking about codes and stuff like that. Yeah. So we do have the ability to do bulk import. So if you gave us your full participant list, right? So we would say let's say it's for depot, you? We would say, okay, they've given us the list of all depots. You know, it's Canada or whatever. And then we would select the Excel template that's applicable to that and we would upload it. Same thing for sites. We would do a bulk upload of your sites if that's required. So yes, this is something that happens in the background. So this, I don't even know if I can do this, but I could show you this.

**00:13:14 - 00:13:24**
I don't know if I have the ability to do it, but yes, the capability is there so that you don't have to manually enter these and it's not an API you need to develop.

**00:13:26 - 00:13:39**
Okay, perfect. Perfect. So just to reiterate back to you, diggers can do bulk uploads of sites and participants for our production environment.

**00:13:40 - 00:13:40**
Correct.

**00:13:42 - 00:13:44**
Okay. Yeah.

**00:13:44 - 00:14:18**
Yeah, the only time you maybe want to consider an API, and I don't know if you do, but let's say you were always adding additional depots, like, you know, on a weekly basis or something, and you wanted the system to always be up to date so that you don't have to have us bulk import it all the time, you could potentially create that API, and whenever you added it to, say, NAV, it would automatically import into Diversys. The previous company I worked for is called Distiller, so I still confuse the two because they're so similar. They're versus.

**00:14:18 - 00:15:12**
Yeah. Yeah, so that's the history that I went through with the team about changes that are made. And, yeah, it's so seldom. The chain actually made the decision in the meeting yesterday that once we're in production, If we have a new site or... new material or something, no, it's going to be an individual. Uh, add-in or adjustment. Um, because it's so seldom that it happens. He's not willing to do all that. So, um, that's why I wanted to revisit it out, because Andre brought it up again in the meeting yesterday and I tried to stop him. But, uh, yeah, how we get ready for production is a whole different path, and not at this point. Uh, do I want to discuss it with the team, how we're going to do it.

**00:15:12 - 00:15:30**
I want them to get in, start testing, find all the bugs and everything for you guys. Um, and then you and I can work on the actual plan of getting ready for production. Yeah, and that's what I told him yesterday, and Shane repeated it back to him, so we shouldn't hear any more. That's great.

**00:15:30 - 00:16:12**
Yeah, and that's why we're doing the training that we're doing and the way that we're doing it because if we bulk upload all your sites, as an example, and then you add a new site in a year from now, your team now knows how to do that. So they can go in and delete a site. They can go add a new site. They can update a site. They can do whatever they need to do within the user interface. So you wouldn't need an API to do that unless your frequency of those types of changes for sites was like daily or weekly or something, right? So if you wanted it automated, you could. But from what we understood from our past discussions, you and I at least, is that, yeah, it's very infrequent that most of these things are going to happen.

**00:16:12 - 00:16:40**
Once your depots are there, you maybe add a new one, I don't know, once every year or something. Same thing with sites and all of that. So that's why all of that stuff that's very infrequent, yeah, you just do it through the user interface, which is exactly why I produced that training document the way I did. Because the team is not going to remember what we just talked about yesterday, six months or a year from now. But they will have a document they can go back and reference on how to add a site.

**00:16:41 - 00:16:48**
Right. That's actually really good news. Just making my notes.

**00:16:50 - 00:17:11**
Yeah, yeah. What we're trying to do is clear the fog and make sure that, you know, we're not chasing down stuff that's not real, right? Because it gets the team out of control thinking, oh, my God, they don't do this, this, and we don't do that, and, you know, we're missing this, and then everyone gets all wound up, and then we realize it's actually never a problem.

**00:17:14 - 00:17:14**
All right.

**00:17:20 - 00:17:30**
So, yeah, we do have the ability to bulk upload your depots and sites and bulk create that. So, yeah, it'll be a one-time kind of thing, and then your team would take it over and manage it going forward.

**00:17:38 - 00:17:49**
Okay, something's going on with your system. So you sent me just a few minutes ago at 9.34 a.m. my time an email called testing feedback.

**00:17:49 - 00:17:54**
Yes, I did. Actually, I thought I was showing it on the screen.

**00:17:56 - 00:18:04**
Well, can I ask a question? Can you go to your sent folder and see how many times you sent it to me?

**00:18:05 - 00:18:07**
Was it sending multiple?

**00:18:08 - 00:18:16**
Yeah. Been happening off and on for a while now and I'm. It's like, Oh, is there differences? Or like.

**00:18:16 - 00:18:38**
Well, I only see it sent once at 11 33, so maybe it's my system's been blacking out and so maybe that's happened, but you know, it only shows sent once. That's weird. Okay, sorry about that technology glitch, I guess, but it doesn't seem to be, uh, my email, sending it multiple times.

**00:18:44 - 00:18:52**
So anyway, since we're on that topic, let me just pull up my screen here. Hopefully you can see it.

**00:18:56 - 00:19:40**
Yeah. Yeah. So the reason I sent you that document is because. The testing feedback is based on actual testing that you guys have done and what the expected result was and what the outcome is. So, for example, the locking of our bills, it doesn't tell us what the use case is for that. It doesn't tell us how you tested it, and it doesn't tell us what the expected outcome was versus what outcome you actually got. And the reason I bring it up is because this is going to be reviewed by Mark and Mohsen, and if it doesn't have that level of detail, they're just going to kick it back, and then you and I are going to go back and forth saying, okay, what was your test case? What were the exact steps you did to test it?

**00:19:40 - 00:20:18**
What was the expected result, and what did you actually receive? So is it a defect? So that's why we may not need to adjust some of this stuff. So I wanted to send that example so that you can coach the team since I just added them all. So I don't want them just going in and plugging in, like, requirements or, like, high-level things like this because it doesn't tell the team anything. And then Mark and Mohsen are going to be trained, basically, to ignore your feedback. And so I'm trying to avoid that by making sure that it's test case. What is your test case? Or, sorry, what is the use case? How did you test it? And then was there a defect? If so, what's the defect?

**00:20:22 - 00:20:23**
Okay.

**00:20:24 - 00:20:34**
Locking our bills and the extrapolation of the mobile phone? Okay, yeah, all right, so locking our bills, okay, yes.

**00:20:34 - 00:21:17**
So if you actually start with your mobile phone one, that's that's a good one. Because, um, because you did test it, I saw you test it, um, yeah, so so your use case would be that, you know? The ABCRC team needs to have two two-factor UH authentication and the UH. The code that gets sent needs to be sent via both email and SMS. And so that's your use case, right? So then you can say, this is how I tested it. And then you would enter a defect because it didn't work. And then they would automatically see that, you know, my team went in or the ABC or C team went in. This was what they tested. This is how they tested. And they're telling us that they found a defect.

**00:21:19 - 00:21:56**
So then Mosen and Mark are going to look at that and go, okay, yeah. So they'll look at it quick, validate it, and then say, okay, so the ABCRC team told us this. This was their feedback. It's going to be in release, you know, the next release or whatever, and so on. So that's where they'll go put in the feedback, which then you and I and the team, mostly Mosen, will get together and walk through all of the items, and they'll tell you, like, on them. Whatever, biweekly or monthly basis, where they're at with each of the defects and whether that's going to be in release four, release five, et cetera.

**00:21:59 - 00:22:56**
Okay. This is going to become an administrative nightmare overhead for me because you're basically wanting me. Okay. So I'll have my test cases. They're assigned to my team members. And now what you want me to do is to copy and paste all those test cases into this system and the results. So I'm going to be doing triple the work. One, creating the test cases. Two, assigning the test cases. Three, getting the test case results back and copying and pasting all that into this form.

**00:22:56 - 00:23:33**
Yeah, I don't think you need to do them all. I think the team only needs to investigate when there's a defect. So you could have your test cases and assign them and so on. So then if they say, okay, I tested this and it didn't work. So then they have access now, and you would instruct them, okay. And you can even ignore the use case for that matter if you want. You can just go in and say, this is the test case. This is what we tested, and this was my expected result, and I didn't get that. So then they would only have to enter the stuff that didn't work. Because realistically, if it works, then we don't care, right? It's good for you. It's good for us.

**00:23:34 - 00:23:56**
What we care about is if it didn't work, we want to know why so we can investigate. So if you had 100 test cases and like five of them had an issue, then there would only need to be those five in, which would say, this is my test case. In other words, this is how I tested it. And this was the outcome. And it's not what I expected.

**00:24:07 - 00:24:09**
If it is what you expected.

**00:24:09 - 00:24:16**
It doesn't matter. We don't need to know. If it works, it works. And so, I mean, if you want to tell us that it all worked, that's fine.

**00:24:19 - 00:24:23**
Successful test cases, yeah, is irrelevant. Okay.

**00:24:24 - 00:25:07**
The idea is so that these guys see your defects as quickly as possible and they can start to plan. Like either say it's a misunderstanding, it's a new requirement. It's already been planned and it's on the roadmap. It's going to keep us well informed of if you guys think there's defects, the team's going to know about it right away. But without the detail of what you tested and how it was tested and what the expected outcome versus what the actual outcome was, then they're just going to punt it back to us. So then it becomes an administrative nightmare because you and I are going to have to go back and forth, back and forth, back and forth. To add that missing detail anyway.

**00:25:11 - 00:25:18**
Yeah. So, okay. I have to have a conversation with Shane.

**00:25:18 - 00:25:26**
Yeah, we want it to be as simple as possible, but we want it to also be efficient so that the team sees it right away and start to address it.

**00:25:27 - 00:25:47**
Yeah, it's efficient on your side, but it's not going to be efficient on our side. Yeah. I'm going to have to explain to Shane how you guys envisioned the testing as opposed to how we thought we'd be doing the testing. Okay, leave this with me.

**00:25:47 - 00:25:54**
Yeah, because when you guys are doing your testing, I can't imagine you're not recording the results, right? Particularly if it fails, right?

**00:25:55 - 00:25:55**
Yeah.

**00:25:55 - 00:26:11**
And so rather than record it somewhere else, you just would record it here. So you could say, these are the test cases, and now when you go in and test it, if it passes, just identify that it passed. If it doesn't, then create a testing feedback case that says, this is what I did, this was the result.

**00:26:14 - 00:26:22**
Yeah. You're going to have to leave this with me. I'm going to have to have a conversation with Shane.

**00:26:24 - 00:26:38**
I mean, because otherwise you're going to have to record how it was tested. You're going to have to validate that the testing, that they went through the right steps and tested the right thing the right way. You're going to have to record what the result was, and then you're going to have to tell us about it anyway.

**00:26:40 - 00:26:40**
Right?

**00:26:42 - 00:26:55**
Because if we don't know about it, we can't help to fix it, or we can't get our QC team on it or our dev team on it. The American Mosin can't plan for it. It can be put into the product if it's not there. I mean that information has to come to us somehow.

**00:26:58 - 00:26:59**
No, no, I understand that.

**00:27:29 - 00:28:12**
Because, I mean, once we know about it, the bulk of the work actually is with Mark and Mohsen. Because if it is a true defect, they need to investigate it, number one, to prove it is a defect. And then they need to start the planning and get the dev team on it and put it into the release and tell us. So usually in here, when it's going to be released or when it's going to be fixed or if it's just a misunderstanding and they'll give the reason why it's a misunderstanding. So, yeah, just so so, it's not a hundred percent. You don't need to put them all in. If it's a pass, it's great you just flag it as as as a pass, but if it is a problem, we need to know.

**00:28:12 - 00:28:25**
How did you test it, what, like, what steps did you go through to test? What was, what did you expect it to do, and what was the actual result? So I included that in that example document I sent.

**00:28:25 - 00:29:12**
Yeah, I haven't looked at the document, I'm just. I'm looking at my test cases. So basically, we're going to be doing testing. Yeah, you're going to, okay. I'm not going to say anything more about this. Yeah, I'm not going to say anything more. I need to have a one-on-one with Shane about the testing that we designed. It's based on what you just told me now. Our testing will not work for what you guys want.

**00:29:15 - 00:29:19**
And so maybe elaborate on that if you could?

**00:29:20 - 00:29:21**
Nope.

**00:29:21 - 00:29:23**
Okay. You won't tell me why?

**00:29:26 - 00:29:45**
It won't work because basically I've got to do all the pre-testing and then give it to the team and get them to test it. So, yeah, with what you guys are asking for, it won't work in our design. So that's why I have to have a conversation with Shane and Sam because I'm not full-time here, right?

**00:29:46 - 00:30:28**
No, no, I know. And the reality is that the way that NCorp is doing it is after every release, They're going through with their list of use cases, they're plugging in how they're testing against that use case and then just telling us if there's defects or not. So they're doing it, like on a release by release basis. But because you guys are only just getting into the software right now, your team hasn't had enough time to go in and play around with it and actually learn it. Yet. That they haven't even had the user training, as you know, so usually after the user training and they get familiar with the system. Then you would hand off the use cases, say, here's the use case, that's what I need you to test.

**00:30:28 - 00:30:37**
They would go through, test it and then tell us if there's a defect. So it wouldn't necessarily be you doing it all, it would be the team. So, like with, Uh.

**00:30:37 - 00:30:47**
You're actually saying something different than what you just said. So just you're cutting.

**00:30:47 - 00:30:52**
I'm going to share my screen, you're cutting out a bit there. I can hear you now.

**00:30:52 - 00:31:42**
Yeah, okay, I'm going to share my screen. All right, okay, so yeah, I did send you guys a copy of my release to, Uh, testing my preliminary stuff. Stream didn't work. Shipping it's like capacity here, right? So the section is shipping module, you know, on the web, right, not on the mobile. Okay, so web-based description what it is, right?

**00:31:42 - 00:31:43**
Mm-hmm.

**00:31:43 - 00:32:31**
Okay, oh yeah. These are no good because I was waiting for the stuff to come out. And then, of course, the apps. I'm going to find a really good example for you. But I remember I sent you my test results for release two. I'm going to find that and pull that back up. But, so, yeah. I understand what you're asking for. Leave that with me. I understand what you're asking for. We have to figure out on our side how we're going to do it.

**00:32:34 - 00:33:01**
Yeah, and the way, like we've given your team access to this, but the fact is, unless they know the software and they've had hands-on and they're playing around with it, I mean, you're probably the most knowledgeable in ABCRC right now with the software. So even if you handed them a use case, they may not know exactly how to do it unless you told them these, unless you created like the test case too and said, these are the exact steps I need you to follow.

**00:33:03 - 00:33:10**
Yeah. So remember we got released three, like March the 1st, right?

**00:33:10 - 00:33:11**
Yep.

**00:33:12 - 00:33:17**
So we haven't had the application that long.

**00:33:17 - 00:33:19**
No, that's all fair.

**00:33:21 - 00:34:18**
So, You've got to remember, your other client is really heavy on the mobile side. So, yeah, they've been playing in the system for a while because the application was meeting their basic requirements. So they got in a lot sooner than we did. So, yeah, so we're only, what, six weeks into the application? That's about it. Yeah, so the first month. How many times was I working with you on the application, right? And providing some feedback? Yep, and so now I'm trying to go into official testing, which is fine. So the team needs to be taught so that they can go in there. So, for example, right after the operations training, the team's going to go in there and they're going to set up. We're going to start with the manual sites to start with, okay.

**00:34:19 - 00:34:48**
So they're going to get those in. So that's going to be the test cases for those. And that should take them into mid-May. And by then, we have the POR working, which will give the ER bill automatic side of life. So, yeah, no, my schedule still works. The question still works.

**00:34:48 - 00:34:48**
Yeah.

**00:34:49 - 00:35:05**
It's just how do I efficiently get you the information of defects? And that's what I have to think about, and that's what I have to talk to Shane about. And we're only talking defects. We're not talking success tests.

**00:35:07 - 00:35:42**
Yeah, correct. I mean, it's great if you want to tell us that you had 100 test cases and 90 passed. The reality is the team really needs to focus on what didn't pass and get to that stuff quickly. So that's really what we need to know. And by the way, this is a proposal, right? This is the way we've done it with other clients is we've had the testing fee. If you want to do it a different way, that's okay. The problem is that then it's dependent on me setting up meetings with Mark and Mohsen to see the information, whereas if it's in here, they see it immediately.

**00:35:44 - 00:37:03**
Okay, so part of the problem is I made an assumption. I made the assumption that when we started our full test cycle, right? So that was after operations training, right? And I got the team going in and doing stuff. I thought we'd be setting up a cadence of defect discussions with yourself and... either Mark Molson or somebody else, where we would walk you through and demonstrate our exact test cases. Because history with ABCRC is, unless we show diverse what we're actually experiencing, we get pushed back. So as much so what I was thinking is I would register the defect in UM, Monday. Com, and then we would meet, we'll set up a cadence and we'd meet and we'd pull it up. And I would replicate the error so that you guys could see it right away, what we did that created the defect, Um, so yeah.

**00:37:03 - 00:37:51**
So we're seeing something, we're saying something similar, that, um, that cadence is, is something that we do. And what we're doing is we're using this feedback board mark and most, and see the feedback of the defects. They investigate it and then we all come prepared to that discussion. And and generally, motion goes through item by item to say, Okay, this, this one. We agree we were able to reproduce it. It's currently planned for phase four release. This one is a misunderstanding, we think, and let me show you why. And then this one is non-relevant for some reason, right? Yeah. And so, yeah, we do do that cadence. We do walk through the line items one by one. But it's taking you guys give us the information of why you think it's a defect. Our team has a chance to investigate it, and then we all come to that meeting prepared.

**00:37:53 - 00:37:53**
Okay.

**00:37:54 - 00:38:03**
Yeah, that's the purpose of it, is that everybody sees what is perceived to be a problem. And then it's validated as, yes, it's a problem, or no, it's not, and here's why.

**00:38:05 - 00:38:12**
Yeah. And this is just SIT testing. It's not UAT testing.

**00:38:12 - 00:38:29**
Correct, yeah, yeah. But, I mean, you can repurpose the test cases for that UAT. Because, like, let's say UAT happens after Phase 4, as an example. The test case, you may want to run through them all again just to make sure nothing broke.

**00:38:30 - 00:38:31**
Oh, yeah.

**00:38:31 - 00:38:32**
Right. So.

**00:38:34 - 00:38:45**
Yeah. OK, leave this with me. I got to have a conversation with Shane. We have to revisit how. We're going to do testing and the win.

**00:38:45 - 00:39:10**
Yeah. Right. I mean, right now it's primarily you. So it's you putting this information in based on your testing. Yeah. Yeah. When the team is is up to speed, it will be the team putting in. Like, I, I did this test, this is how I did it, and this was the the defect that I came across. Yeah, so yeah, it's not, it's not intended to dump dump the load on. DAV.

**00:39:10 - 00:39:33**
Well, my concern is there's going to be so many devil. And well, never mind, I gotta think about this, uh, and we gotta, I gotta discuss with Shane how we're going to do testing. Yeah, and this does change our yeah.

**00:39:33 - 00:40:25**
And the reason I sent you that document is is because with without enough information that the team can't really do anything. So like, and I'll use locking our bills as the example, like, Mark will look at that and go, I have no idea what, that, what that's referring to. Uh, how was it tested? Have they proven that we lock our bills? And the fact is, even for today's meeting, because the locking of our bills has been raised as an issue. So the information I got back from Mark was there seems to be a misunderstanding, says we don't lock our bills from being paid even though it has gone through QC. As long as all the items have been received in QC, then the R bill can move to claims ready. So he's saying that's probably not a problem. We're going to discuss it this afternoon, but that's the initial feedback so far.

**00:40:26 - 00:40:34**
That doesn't make any sense because that's contradictory to what Mohsen told us, which is why the concern was raised.

**00:40:35 - 00:40:54**
Yeah, so I would take what Mark says over what Mohsen says, but he says exactly, I'll read it exactly to you. It says, namely, so it says, I see some misunderstandings here. Namely, we do not lock. And our bill from being paid, even though it has gone through QC as long as stop.

**00:40:54 - 00:40:59**
Stop, stop, stop. Okay, that first sentence there. Yeah, say it again.

**00:40:59 - 00:41:05**
It says we do not lock our bill from being paid even though it has gone through QC.

**00:41:05 - 00:41:18**
Okay, so there's a problem right there. So the our bill has to be claims ready for payment as soon as it comes in, even if it's selected for QC.

**00:41:18 - 00:41:27**
Right. So the second part of that says, as long as the items have all been received in QC, then the error bill can be moved to claims ready.

**00:41:29 - 00:41:36**
Well, no. See, that's where the problem is. I need to move it to claims ready even before I start the QC process.

**00:41:38 - 00:41:49**
But all the items, what he's saying is all the items have to have been received in QC. So if you have an item... hasn't been received in QC, then you can't move it to claims. Ready.

**00:41:49 - 00:42:08**
Okay, so the shipment comes in and the article comes in and it's identified for QC, right? So they scan all the bags. And that our bill is then needs to be paid even before it goes over to QC.

**00:42:08 - 00:42:17**
Okay, so that might be the issue. So if you can validate that or confirm that that is the case, then that's where the disconnect is.

**00:42:18 - 00:43:23**
Yeah, that's what I've been trying to communicate back, is that in a QC workflow, the R bill is received. It's received at Monday at 9 a.m. They have to pay that R bill that's selected for QC Monday night. In the system, diverse system, I have to send it for payment, even though I don't have. She made the QC results okay. And what Molson taught us is, we have to click on Claims ready to move it into the transfer Uh section, right? And then we have to transfer it to NAV. And pay that that night. Then, you know, through the course of the day, or maybe the next day. The QC process happens, and that's where adjustments are made. That then has to be sent to the transfer in Diverse that I then have to send to NAV.

**00:43:24 - 00:43:45**
NAV does the calculations. It then sends back that data to Diverse, and so that R bill needs to have that adjustment. So you're looking... You can look at the two days, three days process in an R bill that's going through the QC cycle.

**00:43:45 - 00:44:40**
Right. And I think that's fine. But what I think where the disconnect might be, so maybe just walk through it again so I'm clear. So you have all these things coming in, right? They're coming in to be received. So as they're being received, your receiver says this item or these five items need to go to QC, right? So you've received them and he's identified them as requiring QC. Correct. So they haven't officially been received into QC. They've just been identified as they need to be QC'd. Correct. Right. So at that point, are you saying that those items, even though they've not been received by QC, they still need to be or the system still needs to allow those items to be claimed ready? Correct. Okay.

**00:44:40 - 00:44:50**
So that's the disconnect because what Mark's saying is your receiver has identified them as requiring QC, but before they can be made claims ready, they need to be received by QC.

**00:44:53 - 00:45:26**
So there's a QC staging area for, I think that's actually what it's called, where the receiver, he identifies these bags have to go to QC and he'll put it into the app going needs QC, needs QC. And then what happens is the forklift comes over, picks that bag up and puts it into the QC staging area. So it depends on the volume that they're doing. In QC, they may not get to those bags until the next day.

**00:45:26 - 00:45:38**
Right. So are those items, Dav, are they scanned by the person, the QC person? So when they're going to receive or QC it, do they scan it and say, okay, I'm receiving this item now into QC?

**00:45:39 - 00:45:43**
They only will scan the bag when they're starting the QC process.

**00:45:43 - 00:45:43**
Okay.

**00:45:43 - 00:45:44**
So in our scenario.

**00:45:44 - 00:45:47**
That's the receiving of it into QC though, right?

**00:45:48 - 00:45:53**
Right. Okay. That could be the next day though. But that R bill had to be paid that night.

**00:45:53 - 00:46:11**
That's fine. So that's technically when it's received into QC, but you're saying even if it's sitting in that staging area, that R bill with that item still needs to be – we still need to be able to put in a claim threat. Correct. Okay. Correct. Got it.

**00:46:12 - 00:46:24**
Yeah, it's right at the beginning stage. Don't quote me on this. I think they have up to three days. To get it into the QC, the actual QC.

**00:46:25 - 00:46:46**
I just want to make sure we're using the same terminology because there seems to be received and then received into QC and there's this space in between. And you're saying that space in between, even if it's in the space in between, it still needs to be, the system still needs to allow those things to be put into claims ready. Correct. Okay.

**00:46:46 - 00:46:47**
So right at the beginning.

**00:46:47 - 00:47:14**
Yeah, okay, so we have this space in between, and what Mark's saying is like, the space in between we don't. We can't work with that. It needs to be put into cues. And don't quote me on that, I'm not saying he's saying, he's just saying. As long as it's received into QC, so maybe if. When I'm talking to him about it this afternoon and I explain, though, there's this space in between received and received by QC. Though. Those items, too, need to be allowed to be put into claims, right? And then we'll see what he says.

**00:47:16 - 00:48:13**
Right, right. So I think right at the start of the process is where the catch is, because we have to pay that R bill that night, even if the QC process hasn't started, we have to pay that. And that's where the extrapolations and the adjustments come in, because they pay the R bill, whatever is received at the dock, they pay that R bill. Then it goes over to QC, QC goes, Okay, I'm going to do this. Our bill today. That's when they actually receive the bags in QC, because there's a contractual obligation there, too, that they have only so many days in which to receive the item in QC. So the so our scenario is the load was received on Monday, it was identified for QC, so that our bill through the system needs to be paid that Monday night.

**00:48:13 - 00:49:24**
The forklift guy goes over, puts it in the staging area, QC finishes their shift. They come in the next morning, which is the next day, which is Tuesday, they go up and they scan the bags. And now they have received it in QC, but that's day two, so they now have day two and day three to do the QC process, so on Tuesday. They go through, they QC all those bags on Tuesday, and they put that information into the system on Tuesday. That data, the QC results, must then be transmitted on Tuesday night to NAV. NAV takes that volume information to that R bill. Makes the whatever adjustments it's doing, extrapolations, adjustments, whatnot. That information then goes back. So Wednesday, the our bill in Diverse has now received the adjustment, right?

**00:49:24 - 00:50:48**
Yep, and then on, yeah, we're doing a single day here, then on Wednesday night. We claims, ready that adjusted our bill, which becomes the ASR, see that adjustment, our bill is the ASR. Yeah, okay. And then they claim, ready that that goes over to NAV, NaV makes whatever payment adjustment, adjustment needs to be done that Wednesday night. Now that our bill has to stay unlocked, that record has to stay unlocked because on Thursday now. The depot has 10 days in which to challenge the QC results. And so if it's challenged, we need to re-QC that R bill. So then it becomes open again. Whatever adjustments are done needs to go to NAV. NAV needs to do its magic and send that. Data back to diverse. And then it becomes. Then it has to be claims ready again to go back to now for the final payment adjustment. Okay, so that's, that's the complexity of QC.

**00:50:48 - 00:51:38**
Yes, I, so from what I understand is based on this discussion, is that as long as it's been received, like regardless, take QC out of the equation for a minute, as long as it's been received, like that R bill's been received in its entirety, it could be or should be allowed to be moved to claims ready. Yes. Regardless of QC and when it's received in QC or whether it requires QC, take that out of the equation. If it's been received, it can be put into claims ready. Correct. Okay, got it okay, good, that's very helpful, dad. Thank you, because now I'm more informed and I can actually go. Uh, when Mark brings that up this afternoon, I can say, Well, actually, it doesn't work that way. Yeah, and I'm not saying that this is the end.

**00:51:38 - 00:51:46**
All and be all. I think the decision is like, are we going to do this? And if we're going to do it, then there needs to be workshops to really nail down what the requirement is and then do it.

**00:51:46 - 00:52:34**
Yeah, yeah. And when we have those meetings, I'm going to limit the people, we're going to limit the people on both sides to be in that meeting. Very focused should be very focused. Yeah, because we've had way too many people. I'm just going to have the operations team basically on my side. I'm going to have Taz and Aaron, that's it, because Aaron's on the floor and Taz is the clerk. Yeah, so Aaron walks us through what happens on the floor, and Tabs will walk us through in detail. Both both are in detail. But what happens on the back end? All those bags are moving through the QC process.

**00:52:34 - 00:52:36**
Okay, cool.

**00:52:36 - 00:52:47**
We don't need David in that meeting. Because it has nothing to do with NAV, right? Because this is the diverse application, not NAV.

**00:52:51 - 00:52:58**
Agreed. Okay, cool. I don't know if you had much more on your side, but I do have a couple things before we end, if that's okay.

**00:52:59 - 00:52:59**
Okay.

**00:53:00 - 00:53:08**
So the meeting that you had suggested dates for the 20th or the 23rd. So I just wanted to check in on where we're at with that.

**00:53:10 - 00:53:10**
Uh-huh.

**00:53:14 - 00:53:18**
I didn't see it pop up on the schedule unless I missed it.

**00:53:19 - 00:53:22**
Oh, wait a minute. I know why.

**00:53:27 - 00:53:35**
I'm guessing it will be the 23rd, but...

**00:53:35 - 00:53:51**
It'll have to be, yeah. I don't believe Sam got back to me. Both Shane and I agreed upon the time date, but Sam did not. I will get you the answer today.

**00:53:51 - 00:53:57**
Okay, yeah, I just want to make sure we get it on the schedules before they start packing up, and then we're going to move it.

**00:53:58 - 00:54:32**
Just give me a few more minutes here. Oh, that's why it's not. Jesus, I don't like this latest update. Geez, you send me a lot of emails.

**00:54:33 - 00:54:34**
I'm trying to keep you informed.

**00:54:36 - 00:54:40**
No, you give me all these action items. I'm trying to work through all the action items.

**00:54:43 - 00:55:25**
Yeah, well, I mean, as we have already discussed and determined, like a lot of the action items, I know there's a bunch that are still open, but, I mean, hardly any of them are really new. Well, I shouldn't say that. The lion's share of them are not new. They've been around for a while. It's just you were tracking them on our side, and we were tracking ours on our side, and now we've combined them. So there's nothing. There's only a few new ones, like in our last couple meetings, which is going to continue. Of course, every time we meet, there's probably actions. But, yeah, the bulk of them are just me going back in history and making sure we haven't missed anything. And if it's still open, I've identified it as open.

**00:55:30 - 00:55:46**
Just putting some structure around it. So, yeah, the lion's share of those items are not new. And as you saw when I sent the original Word document, which was probably like a month ago now, I actually put in the source. So where did that action item come from?

**00:55:50 - 00:56:08**
Yeah, I need to find an email. I will get you an answer today. I think what I'm doing is Sam hasn't responded. I think that's where my problem is. Because otherwise, yeah, that would have been on there because I remember having the conversation with Shane already.

**00:56:09 - 00:56:14**
Yeah, I just didn't see it and I was like, okay, something's got missed because we're getting closer.

**00:56:16 - 00:56:21**
Yeah, I forgot to follow up with Sam.

**00:56:23 - 00:57:10**
No problem. I just wanted to call it out while we're here. Thank you. Yeah, I think that's it. So, yeah, just. And you already touched on the integration stuff, so I had that as an item to talk about. So, like, when, like, what have you heard back from your, uh, your vendors and stuff like that? I know you were working with them and meeting with them, so so it sounds like you. You guys are working on the what is required and then that'll be followed by the when we can expect it all. So yeah, because that's going to feed into this discussion we're having about the NAV stuff, the NAV data being into Diverses. So we want to try to align those things that when the API is done, that's available at the same time.

**00:57:10 - 00:57:23**
Oh, so this meeting that you and I are trying to set up, is that the same request that Roger sent Shane and Sam for a meeting.

**00:57:24 - 00:58:20**
I think it's different. Roger wanted to have basically a one-on-one with those guys, but our meeting is the whole team meeting to go through the presentation that was shared. Sam had some feedback and stuff, so we wanted to make sure that we've addressed all those items. I think we have. With the exception of the nav data stuff, which we're still working through. But I think the other items we covered off, like you and I talked about yesterday, the batch processing versus the live posting. So that's on the roadmap. I'm pretty sure I included that in there. I think one of the other items was the, are we able to support the manual QC? Versus so the target, target, random, target, and manual? And the answer is yes.

**00:58:20 - 00:59:10**
And by the way, I know you brought this up before, is we're not expecting you to sign off on it because we know QC is not complete yet. So it's just that we want to make sure that it's understood that it is there. It's just maybe not complete yet. So it's there and working. So, yeah, we're not asking for a QC sign-off. That will come later on when the QC is done. And I believe most of that will be delivered in the next release. So that's good. Yeah. The other item was I know we focused on that we had put in the driver application and it's not applicable to you guys. So you seem to be a little bit stuck on that one. Basically, Marks, that was Mark's live, and all Mark's saying is like, this is what's in the release.

**00:59:10 - 00:59:23**
Now. Whether you guys are choosing to use it or not is kind of irrelevant. But yeah, I think that was it. I think we addressed most of the items.

**00:59:23 - 00:59:31**
Do you remember the high level when you sent me that executive meeting request?

**00:59:32 - 00:59:37**
I sent you the dates back.

**00:59:38 - 00:59:49**
Yeah, but what was the date of the email? I wonder if I have an email problem because I'm not finding any 2026 emails in my sent folders.

**01:00:07 - 01:00:16**
So you sent a message to me saying you discussed it, and you gave me the April 20th, 23rd dates, and that was on the 9th of April.

**01:00:18 - 01:00:20**
Okay. Just give me a second.

**01:00:52 - 01:01:09**
So my response to you was the 9th of April at 11.19 a.m. higher time, I guess. So that's probably 9.19 your time. I can resend it if you want, Dad.

**01:01:13 - 01:01:56**
No, I'm looking for the SAM response because, yes. I said, yeah, you sent me your times. And I sent over to Shane and Sam saying, what is your availability? And that was last week. That was on the 9th. And Sam, Shane responded, but Sam did not. There's the catch. Okay. I've got to follow up with Sam today. Okay, yeah. Yeah, I've got some time for Shane.

**01:01:56 - 01:02:01**
My concern is that we leave it too long and then the schedules pack up and we need to adjust.

**01:02:03 - 01:02:04**
Yeah.

**01:02:06 - 01:02:22**
Anyway, let me know. Or we'll go ahead and put it on the schedules or maybe just check with me first to make sure that the schedules are still good. Should be. Doesn't hurt to check. Double check.

**01:02:23 - 01:02:23**
Yeah.

**01:02:25 - 01:02:38**
Well, I can tell you right now that Roger's pretty clear on the 23rd. Let me check Mark. Mark is as well. Yeah, so we're fine with all those times that I sent you. They're still there.

**01:02:40 - 01:03:14**
Let's do the 23rd. Just one sec. Yeah, don't run away yet.

**01:03:14 - 01:03:20**
No worries. I think I'm good right now. Let me just check. I don't think I'm late for anything.

**01:03:24 - 01:03:26**
No. Oh, okay.

**01:03:32 - 01:03:34**
And we wanted an hour, right?

**01:03:35 - 01:03:48**
Yeah, probably. I'm anticipating there may be some discussion. Hopefully it's settled down a little bit, but maybe not. I know it was like swatting a bee's nest, right?

**01:03:49 - 01:03:50**
Yeah.

**01:03:50 - 01:03:57**
Whenever you pointed out that the project's not all roses yet, we need to get it there.

**01:03:58 - 01:03:58**
Yay.

**01:04:03 - 01:04:23**
I think we've made pretty good progress. I'm speaking for myself, but I think you and I are pretty well aligned now on the action items and the risk registers and talking about testing feedback, even though the feedback from your team won't be until a bit later. We're putting all the pieces in place so that it's pretty tightened down.

**01:04:25 - 01:04:32**
Sorry to interrupt. So Roger and Mark should be invited to this meeting too, correct?

**01:04:33 - 01:04:33**
Correct, yeah.

**01:04:34 - 01:05:00**
Okay, it's coming out right now. I'm making an executive decision on Sam because Sam was the one who did not respond and I forgot to follow up with Sam. So there we go. So it's on the 23rd at 9.30 just because of the way our weathers are going and people trying to drive in. 9.30 would be better in case the Deerfoot is posted again.

**01:05:02 - 01:05:06**
9.30, so that's 11.30 our time. Yep, that's fine.

**01:05:06 - 01:05:09**
Yep. Perfect.

**01:05:09 - 01:05:18**
Yep, it's all good. Roger's good at that time. Yep. And Mark is as well. Yep. It's all good.

**01:05:19 - 01:05:24**
Okay. All right. It sounds like we solved world hunger today.

**01:05:25 - 01:05:39**
Yeah, yeah. We're making pretty good progress, honestly. I think we are. I mean, we've got our fair share of bumps in the road to go through, and I'm sure there will be a few more. But, I mean, at least we're able to talk about it and have a conversation and work through it.

**01:05:41 - 01:05:47**
Yeah, the project meetings are a lot more effective than what I had with the other three gentlemen.

**01:05:49 - 01:05:56**
Yeah, I hope so. I put in the effort to make sure they are, so I hope that's coming out.

**01:06:03 - 01:06:25**
What we will do? Okay, so are we going to put anything together for the executive meeting or are we? No? They want. Do we want to use? Well, let's not muddy the water.

**01:06:25 - 01:06:36**
Yeah, I mean, if if you wanted to share like, what, what the remaining concerns are in advance, that would be helpful. But I mean, you don't have to. It's a discussion.

**01:06:36 - 01:07:36**
Sam already did, Sam already did, um, and I'm keeping Sam and Shane updated as each. As we go forward. Of course, there's new information that comes up that, um, sort of changes. What the status report you guys produced from your end? My argument to Sam was it was a status meeting or status report. From the vendor's perspective, Sam. And to me, yeah, it was totally from the vendor's perspective. Now, if you have a different interpretation or a different view of the project, that's totally different, and hence why he sent out those emails to you. So let's not muddy the water. Let's go with what Sam has stated, and let's get clarity. Let's get Sam clarified. And secure in that this project is moving forward in a successful manner.

**01:07:36 - 01:08:16**
Yeah, yeah, I think the other thing too, in my response to Sam, and maybe it's something you want to, um, float around internally. There was like, Is that the right format for? For the executive meeting? One? I think we should continue on with, uh, with the executive meeting, so let's figure out a cadence for that. Is that is monthly too much is is. Should we do it every two months? Should we do it once a quarter? I think not doing it at all is is a problem. And then, like, is the format correct? So we're sending a Powerpoint presentation, you know, that's, it's high level, it's what Roger had asked for to be, like an executive level. But it sounded to me like Sam wants a little bit more detail, and if that's the case, then that's fine.

**01:08:16 - 01:08:20**
You and I can work that out, make sure we collaborate on it and then we present it together.

**01:08:20 - 01:09:01**
Right so I can address. What are your concerns right now, or questions or whatever? Uh, yeah, so. Because you guys sent out that status report, Sam had the reaction. In my discussion with both Sam and Shane, I pointed out, well, look, let's go back to at least right now, monthly executive steering. And starting in September, you've got to make availability for biweekly because the project will be moving a lot faster in September. Because we're going to get hit with slowdowns on my side because we're into their busy season and vacation, right? Right.

**01:09:01 - 01:09:18**
And that's where we need to keep the project schedule up to date, which is another thing that we're going to have to make some time for. Because I know there's some things in that project plan that I shared with you that's missing. Reports, I think, is one. So we want to start to plug those things in and see what it actually looks like, right?

**01:09:20 - 01:09:24**
Yeah. Okay. Tomorrow, I'm already slammed.

**01:09:25 - 01:09:39**
Because the project plan right now is basically like we've forecasted dates or put in dates on your behalf. And I think we need to have you guys check to make sure that that's actually realistic. Right.

**01:09:39 - 01:09:41**
What is your Monday like?

**01:09:42 - 01:09:58**
Monday is the 20th. I have meeting in the morning, my time. That would be 7 a.m. your time. So I'm good from 10 a.m. my time, which would be 8 a.m. your time, right through until noon.

**01:10:01 - 01:10:13**
So you can do, oh, noon. So 11 plus 2 is 1 o'clock. So 9 is 9, 10, 11. So 9 o'clock works. Oops.

**01:10:14 - 01:10:17**
9 o'clock your time would be 11 a.m. my time. Yeah, that works.

**01:10:19 - 01:10:26**
Okay. Now, I'm setting up a meeting between you and I, and we're only allowed to talk about one thing.

**01:10:26 - 01:10:27**
Project.

**01:10:28 - 01:10:33**
Gotcha. Project schedule. Yep. Nothing else. Unless, of course, the world blows up.

**01:10:34 - 01:10:37**
Hopefully not. It was shaking the hell out of things, though.

**01:10:38 - 01:10:40**
Wow. Yeah. There we go.

**01:10:41 - 01:10:46**
That totally caught me off guard. We were on the call with your team, and I was like, holy shit. What's happening?

**01:10:47 - 01:11:03**
Yeah. So, yeah, so that Monday we're going to walk through and come to an agreement of our schedule because that's going to be discussed on Thursday anyway. So we can go through, and then if we have to do any fine-tuning, you and I have our Wednesday meeting that we can do fine-tuning on.

**01:11:03 - 01:11:16**
Yeah, yeah. So, again, there's stuff in there. There's forecasted dates, but there's probably some stuff that's missing, and that may affect the dates. And so let's try and get it to be as realistic as we can.

**01:11:17 - 01:11:17**
Yeah.

**01:11:18 - 01:11:46**
I don't want to present it on the 23rd and everybody looking at it saying, okay, this is the agreed-upon schedule, and then to find out that you guys haven't looked at it or plugged your data in and don't agree with the schedule. I think that's going to look terrible for both of us. So it's a starting point. It's basically a template, and I know there's some things missing. So let's round it out and make sure that we're in agreement and it's solved.

**01:11:48 - 01:11:48**
Exactly.

**01:11:49 - 01:11:53**
Okay, very good. I just accepted your meeting invite. You should be all good.

**01:11:54 - 01:11:58**
Okay. Sounds perfect, sir.

**01:11:5
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="42fc0c173dbb734e">>>
</file>
assistant: Done.

Created:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-15 Dav Duane Data Integration, API Development, and Project Management Discussion.md`

Send the next one.
user: [media attached: /home/duane/.openclaw/media/inbound/2026-04-14_ABCRC_Training_Feedback_and_Software_Requirements---989d379c-3fb3-4809-a87a-f65ecece2eab.md (text/markdown) | /home/duane/.openclaw/media/inbound/2026-04-14_ABCRC_Training_Feedback_and_Software_Requirements---989d379c-3fb3-4809-a87a-f65ecece2eab.md]
[Discord #alfred-main channel id:1478436599074258954 +4m Thu 2026-05-07 13:32 UTC] Leitchy (dl_70): <media:document> (1 file)

<file name="2026-04-14_ABCRC_Training_Feedback_and_Software_Requirements---989d379c-3fb3-4809-a87a-f65ecece2eab.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="5ac8732772fff197">>>
Source: External
---
# 2026-04-14 ABCRC Training Feedback and Software Requirements Discussion
Creation Time: 2026/04/14 13:56


## Transcription

**00:00:00 - 00:00:01**
You're going to do something?

**00:00:03 - 00:00:04**
I'd have. Wow.

**00:00:06 - 00:00:09**
Shane's just leaving. He's actually going to go do his job.

**00:00:11 - 00:00:13**
Thanks for joining, Shane.

**00:00:19 - 00:00:19**
Okay.

**00:00:20 - 00:00:22**
A little bit of feedback for you on that training.

**00:00:23 - 00:00:23**
Yep.

**00:00:24 - 00:00:25**
You heard Andre?

**00:00:26 - 00:00:26**
Yep.

**00:00:27 - 00:00:32**
Okay. When we do upgraded training, it'll get worse. So just a heads up for that.

**00:00:32 - 00:00:45**
Yeah. Yeah. Okay, cool. I think it showed how aligned you and I are. I think we made a good team, to be honest, is my input.

**00:00:45 - 00:00:45**
Yeah.

**00:00:48 - 00:01:17**
I think that came across pretty clear how aligned we were. So I think the work that we did up front to... you know, build the training, review the training together and so on, I think, and and devise what the the training rollout should look like. I think came through pretty clear. It was a bit rushed towards the end because, as you said, uh, Andre was a little bit like trying to corral cats. But uh, he's his heart's in the right place, he sees the end result. He's. And he's trying to get there without understanding the building blocks first.

**00:01:19 - 00:02:04**
So with Andre, he keeps bringing NAV into play and he keeps bringing in the mass importation. And we keep telling them, don't bring NAV. Don't talk about production migration. It's not in scope. Just learn the application. And so Aaron's in the call because Sharif, Aaron is Sharif. Sharif is Andre's counterpoint. Sharif is on medical leave. Aaron is in the call. Because he's representing the Calgary plant. Taz is the depot manager, right? Yeah. Yeah, so with everybody switching roles and everything, that's why Aaron's in there. And so Aaron and Clive are going to be the ones who are going to train on the scanner.

**00:02:05 - 00:02:08**
Right, yeah. Makes sense.

**00:02:12 - 00:02:15**
All right, you're a little bit upset about my comment about the R bill.

**00:02:16 - 00:02:19**
No, not upset, just digging for more detail.

**00:02:21 - 00:02:22**
Yeah, sorry.

**00:02:24 - 00:02:42**
Just to clarify where you said there's a lot, and so it's pretty broad, so I'm just seeking to understand what is that, like what's all included in a lot, so that I can basically have an itemized list and figure out how I can help you.

**00:02:43 - 00:02:56**
Yeah, I'm trying to get to put it into our monday.com. I just haven't managed to get there yet because somebody sent me, what, 65 action items on Friday?

**00:02:57 - 00:03:16**
Well, most of them are already there. I think we put in a few extras, but, yeah, it wasn't. Anyway, yeah, that's all I'm seeking to understand is what's included in a lot. Because I know we're aware of the ASR stuff and the contention there.

**00:03:18 - 00:04:32**
Thank you. Sorry to interrupt. Before I forget, because it finally dawned on me, the ASR and the R bill are the same thing. The difference is the ASR has the extrapolation data. So the ASR is the original R bill with just the extrapolation data and the financial data. That's what it is. Right. So if the R bill, and so this is part of the allot, if that R bill is locked out that once it's claimed ready and cannot be adjusted, the volumes between NAV and diverse will diverge. So it has to be able to have the extrapolation data brought back into that particular R bill that's claimed ready and adjust that appropriately. And that's what I'm trying to get into monday.com. So the ASR, and I think where Mark, I know there's a meeting.

**00:04:32 - 00:05:03**
I think the part that Mark missed was the fact that the ASR is actually the R bill. With the extrapolation data, so if Diverse can do the extrapolation and adjust that into the R bill, then we're fine. But if it can't do that, it needs the ability to import the expert extrapolation data into that particular R bill.

**00:05:03 - 00:06:00**
Right, yeah, and I think Mark understands that based on the previous conversation, but I think the resistance was that that additional data that comes back from NAV, it was like, I don't know, one or two fields. I think it was two fields. It wasn't significant. It was a couple fields. So Mark's contention was that right now within the framework of the software, that those two fields don't fall anywhere within that framework. So it would basically be a customization of the software to include those additional fields. And he was saying it was something like for 10%, like 10% of these things, like 90% are fine. It's the 10% that requires some sort of adjustment or whatever. And because that ASR report is already being generated in...

**00:06:01 - 00:06:43**
NAV, did it make sense for that data to be pushed back into Diversys to have the ASR report generated there? And I think that's where the two teams were diverging on. Mark was saying you're already doing it in NAV, so we just push the information that we have associated with the ARGO into NAV and you have the additional fields and produce the report there. Why would you need to push the data back into a diversus? And I think that's the piece that he didn't understand or doesn't understand still that he wants to get clarity on. So that's where the friction is. Because David's saying, no, this is the requirement. It has to be there. And Mark's asking, but why?

**00:06:45 - 00:06:46**
You're right.

**00:06:48 - 00:07:11**
Sorry, the other thing I'll add just before you take over. Is that I believe in the conversation he was indicating that at this point, if it had to be done, we don't know how much additional dev time it would take to put it in there. And so if it does take additional dev time that's not been planned for, then we have to look at how does that affect the overall project timeline.

**00:07:12 - 00:08:20**
So here's the nastiness about this. So well before you came into play, and even before I came into play, but I know it came into play in December of 2024, the ASR extrapolation data, okay, we're talking about the extrapolation data, has to be reflected back into diverse. If it's not, the diverse volumes will be out of sync with NAV. And that's the critical piece there, is if diverse does not take back the extrapolation data, whether it's positive or negative data, it will become out of sync with NAV. And that's the critical piece. Forget financials, forget printing out a report. That extrapolation data for the items that is done through QC, that has to be reflected back into that R bill. Otherwise, the team cannot rely on the R belts. Right. There's the catch. Yeah.

**00:08:20 - 00:08:45**
So I think that maybe is the detail that didn't come across in the meeting. Right. I think we understand why. It was a little – it got a little heated and people stopped listening. Yeah. But that's the clarity that I think the team needs. And then we can take it away and say, okay, now we've defined it as like a mandatory requirement, so now you really need to take a serious look at it and tell us how it affects the project overall.

**00:08:47 - 00:09:50**
Going back to Mark, Mark got caught up on the fact that the ASR had financial data as part of the report, but the ASR was a report. It wasn't the actual R bill, right? So the ASR is an R bill, whether it has extrapolation data or not, but it's the R bill, just with those extra columns. And in the experiment I was doing between NAV and DIVERSE is my volumes became out of sync very quickly. And so if we're supposed to use diverse as the volume record, the book of records, we can't because the volumes are out of sync. So that's the critical piece, and that's what the allot is. Like, that's a lot of shit there that's critical on that particular R bill.

**00:09:51 - 00:09:51**
Okay.

**00:09:51 - 00:09:57**
Right? Forget about printing something off. We have to figure out how we get that data back in.

**00:09:58 - 00:10:46**
Yeah, to make sure they're in sync. Okay, that makes sense. So if that's what a lot is, then I get it. It's just my understanding, and I didn't want to jump to a conclusion, was when you said there's a lot missing, or I forget how you phrase it, there's a lot now missing based on what we saw or we know. And I was like, okay, so what else have they identified as missing in the software? And that's the itemized list I was looking for. I want to be able to take it back to the team and say, okay, these are the five things that the ABCRC team has identified as critical to their program and missing from the software, and so what are we going to do about it?

**00:10:48 - 00:11:51**
The extrapolation data is the item that I found to be critical. Other parts of that a lot is I can't tell you what, how do I explain this? When I showed the team the R bill, all right, when I demoed Diverse to them, they're the ones who were saying, well, it's missing this, this, this, this, this. And I thought, well, okay, hold on a second. What I wanted to do then is that's why we had the training session set up. I want them to go in. Start using the application and then what I want them to do is to fill out on Monday.com, Uh, the testing feedback. Okay, yep. But it is agreed that the most critical thing, which is why I wanted to bring it to your attention, is that extrapolation data has to be reflective in the Our Bill, and therefore, the Our Bill can't be a locked record.

**00:11:52 - 00:12:12**
I have also learned that there are other adjustments that are done that also affect the R bill. So the other critical piece was the locking of the R bill as claimed ready, not being able to be modified after the fact.

**00:12:12 - 00:12:13**
Okay.

**00:12:15 - 00:13:21**
That's good. So that's the critical. There's a lot of other stuff that the team is saying. I don't actually have my head wrapped around it. I thought, no, let's let the team get in there because we're so close to training. So stage one of training. I'm sure I've told this to you before, but I'm going to reiterate it. I have 26 currently manual R bills. These are R bills that don't come through the POR system. There are manual depots. The team is actually, after the operator training, is going to be keying those R bills into diverse. So they're mainly going to be doing it just like I did before, and that's when they're going to actually pick up, you know, is the R bill area, the transaction area, missing critical items.

**00:13:22 - 00:14:11**
You know, they can put down, hey, it would be nice to see dancing elephants. That's fine. But is it actually missing critical fields? And they will be able to identify it. Because if I take the R bill and look at an existing R bill, it pretty well matches up. However, if I take an adjusted R bill to the diverse R bill, it doesn't match up. I forget the field or the column. And that came from Andre, so I was scratching my head a little bit more. He said that was pretty critical. But that's where the law is coming from. My point is extrapolation data, but from the team, I want them in there and I want them to record it into the testing feedback so you guys can decide, you know, is this really critical?

**00:14:13 - 00:14:25**
Does it prevent operational function? So I want the team to do it and then I'm going to be reviewing it with the team and saying, is this really a critical item or is it a nice to have item?

**00:14:25 - 00:14:27**
Yeah, or just a misunderstanding. Yeah.

**00:14:28 - 00:14:29**
So, yeah.

**00:14:29 - 00:15:09**
So that makes all makes sense to me. And I think that's the reason why the feedback board was created so they can get in there and plug that information in. And we already have that as an action item. And one of the risks is that right now we haven't received that. So when we receive that feedback, is that going to result in more development work that's required? Maybe. We don't know yet, right? So that's why it's a risk is we don't know. Maybe it won't, but it's possible that it could. And so, yeah, getting in and doing that. So I think we're aligned there. It's just the new information based on the pushback from ASR. When you said there's a lot that's missing.

**00:15:10 - 00:15:56**
I'm just trying to really understand because the team wants to meet tomorrow to talk through all of those items that are identified as missing. So if it's just ASR primarily, then great. If there's more, though, like now is the time to tell me because they want to meet tomorrow afternoon to go through and make some decisions on, like, okay, based on what we know about ASR and their requirement, you know, can we just do it? And as you know, I can't make that decision. That's up to Mark and Dejan. But my push is going to be for you guys because my job is to represent you guys and say, like, this is a requirement. Like, you have to do it. You have to figure out a way to do this. It's mandatory. And here's why.

**00:15:56 - 00:16:03**
So that's where I need your support and your information is, like, why. Like, what is missing and why is it important?

**00:16:05 - 00:16:22**
So far, the one that I can stand behind from my team is the missing information from what we call the ASR report that has to be reflected back into IVERS. That is the critical one.

**00:16:22 - 00:16:24**
We call it the extrapolation data.

**00:16:25 - 00:16:54**
The other ones, there was a couple that... They're like, this is critical, this is critical. And I'm like, is it really critical? Because that's going to change the R bill structure. Is it really critical or is it nice to have? For example, it's critical to have a QR code. Why? What's the point of a QR code on an R bill?

**00:16:57 - 00:16:58**
Yeah.

**00:16:58 - 00:17:18**
Well, they couldn't give me. Yeah, so they were supposed to. So all the points that they brought up from the demo, they were supposed to put it in writing why this was critical. The only thing I got back from them between the time I made that statement to you and today is the extrapolation data.

**00:17:18 - 00:17:27**
Yeah, okay. Yeah, it just scared me a little bit when it said, you know, based on what we now know today, there's a lot missing. And I was like, oh, no, it's a lot.

**00:17:30 - 00:18:27**
I also think with today's training session, so I've been doing my best to get them out of NAV. Diverse is not NAV. NAV is not diverse. You heard in the beginning, Andre kept referring to all the fields that are in NAV. Well, it's irrelevant. This is diverse. So some of the stuff he thought was critical yesterday afternoon, I walked them through it and they're no longer critical because it was critical in that it's not critical in diverse. And so that's what I'm waiting through now from their initial statements that, Oh my God, it's missing. I can't remember the number, but it was like 10, forget the ASR stuff, but there was like 10 critical items. And I'm like, how did we miss this? But working through them, you know, tell them, put it in writing.

**00:18:27 - 00:18:37**
Why is this critical? The only thing I got back was the extrapolation data. So it's like, guys, don't tell me this is critical. And then you think about it and go, yeah, it's not critical.

**00:18:38 - 00:19:19**
Right. Yeah. Yeah. That's where I was coming from. It was like I need to meet with Dab right away to understand the list, the itemized list of what's missing. And so if it's just ASR, and honestly, I thought that was my opinion. I said, I think it's just ASR. I mean, I know we're well aware of other things, like S-Bill needs to be created, and C-Bill needs to be, and QC needs to be completed, all that stuff. We're aware of all of those things. But this seemed to be, like, a new revelation. Like, all of a sudden, we went in, we looked at a bunch of stuff, or we saw the demo from MOSA, and then, like, there's 10 other, 15 other things that are missing.

**00:19:21 - 00:19:27**
Well, that is a true statement, but are they critical? To warrant massive changes, I'm not so sure now.

**00:19:27 - 00:19:53**
Yeah, yeah, yeah, so so if you could send me a list of what you believe is is, like, included in the law, then that's what I can take to the meeting tomorrow with, Uh, because I'm meeting with the CTO, Dan, I'm meeting with Mark and and Roger's joining the meeting. So I want to be able to properly represent what what ABCRC believes is is missing, and so if it's just that's fine.

**00:19:55 - 00:20:45**
Yeah, at this time, that's all I'm going to put because I'm not so confident that the other items that they brought up are, I don't believe, I don't, I can't stand behind them and say this is critical or mandatory other than the ASR. So that was the only one I was actually going to put in. The testing feedback to you is the extrapolation data. Yeah, okay, other items cool, the other items, I think it was 10, the other 10 items matter of fact. They got a ping after the meeting. I now know that we're down to nine items based on what they saw today. All right.

**00:20:45 - 00:20:48**
That's good, less is better. Okay, yeah.

**00:20:48 - 00:21:14**
Uh, so, from an initial brush and understanding. I'm not so sure about the other nine. The ASR, yeah. There was something else, too, that just came up yesterday that had nothing to do with the R-Bell. Okay, yes. Latch processing versus real-time.

**00:21:15 - 00:21:15**
Yep.

**00:21:18 - 00:21:34**
The question that was asked to me yesterday, and I couldn't find the answer. When do you think real time will be in play? Like, are we talking 2026, 27?

**00:21:34 - 00:22:01**
Yeah, no, when I talked to Mark about that item specifically, and I have, he told me it's in phase four. So that should be the July release. I think I put that in the message that I sent back to Sam. I think I put that detail in. I don't recall. I think I did, but yeah, that's that's, uh, I don't know if I put the specific date or I just said it's on the roadmap. But um.

**00:22:01 - 00:22:11**
You're, uh.

**00:22:11 - 00:22:13**
Sorry, you're cutting out right now.

**00:22:13 - 00:22:32**
Oh, yesterday I was in on the whole day session with Sam and Shane. Because your project status report created quite a.Stir. So we're working through things. Yeah, I can't find the email you sent to Sam, but...

**00:22:32 - 00:22:42**
Anyway, Mark said it's in phase four, so July, the July release, end of June, July release.

**00:22:46 - 00:22:54**
Yeah, so for right now, you're meeting with Mark and CTO? Because the extrapolation data has to be returned back into Diverse.

**00:22:55 - 00:23:28**
Okay. If you could go through the list of items that you have, and by the end of the day, if you can just shoot me an email in case anything else needs to be added, just so I can go into that meeting with the list and just include, for the ASRP specifically, the why. So that I can properly articulate that to the team. Like this is from the customer's view of why this is critical to them. And so what's it going to take for us to do it?

**00:23:29 - 00:23:37**
Right. Because the statement yesterday is if you guys can't do it, we've just paid for a very expensive RBL server.

**00:23:38 - 00:24:19**
Right. Yeah. I mean, my push is to say, yes, I understand there's been pushback and we're trying to understand the why. Why can't you continue doing it through now? If the thing is that if it's not pushing the data back or we're not receiving the data back and it's putting things out of sync, then something's broken. And, of course, you can't work that way. So if they have to be in sync and it has to be pushed back, then we have to figure out a way to do it. And that's basically going to be my message is, you know, I understand that maybe it's only 10% of the time, but it means 10% of their stuff year over year is wrong.

**00:24:27 - 00:25:10**
So, yeah, if you could do that for me, Deb, I would appreciate that a lot so that I can properly represent your points tomorrow in the meeting. Because my push is for them to actually take it serious and put it into the plan. And they may come back and say it's an extra month of development. So one of Sam's questions, which I said is plausible that there might be additional phases. And we know that phase four is completely like packed with stuff right now. So if this is something that needs to be done and, and maybe they can put it into phase four, but it probably means something else needs to be bumped out into another phase. So, so our job then is to understand what are the impacts to our schedule?

**00:25:12 - 00:25:23**
And so they say, yes, we have to do it and we're going to do it. And this is what it's going to take to do it. And then we have to figure out, okay, how does that, How does that hit us?

**00:25:24 - 00:25:39**
Right. So it doesn't need to be in the July release because here's the catch to the extrapolation data. In order for the extrapolation data to get into Diverse, we have to create our APIs.

**00:25:39 - 00:25:41**
Yeah, there needs to be the integration, yeah.

**00:25:42 - 00:25:54**
So that's the connection there. So does it need to be in for the July release? Absolutely not. Does it need to be in there and tested before we go into production? Absolutely okay.

**00:25:54 - 00:25:58**
Yep, that detail is good as well. So yeah.

**00:25:58 - 00:25:58**
Yes.

**00:25:58 - 00:26:25**
Because I just want them to make the right decisions. And and you know, the if he's pushing back just for the sake of pushing back because he didn't like the way Dave had presented it. That's not a good reason, right? And and in all fairness to Mark, I I think it may not have been presented, um, clearly as well. So so I think there's, there's shared, shared blame to go around, but I mean, you and I are looking for resolution. So that's, that's what we'll do.

**00:26:29 - 00:26:48**
Matter of fact, I'm updating. Ah, can't spell all of a sudden. I'm updating the, uh, TC08, by the way.

**00:26:49 - 00:26:55**
Okay. TC08.

**00:26:57 - 00:27:01**
Good question.

**00:27:04 - 00:27:25**
I'm just wondering about the TC, where you're seeing the TC. Well, in the testing feedback. Oh, testing feedback. The first letter. Okay, yeah, no, no, you're okay, cool, no, that's fine. I was thinking, TC like, are you updating the action items? It should be in a.But okay, I got you.

**00:27:25 - 00:27:36**
Because it was through testing that it finally made sense of where the misconnect between Mark and David occurred.

**00:27:48 - 00:28:06**
Yeah, there was a clear disconnect, and then that spun out a little bit on us. Anyway, I don't think it's anything we can't recover from, and that's the purpose of the meeting tomorrow is to find a solution.

**00:28:26 - 00:28:27**
What I put in there, Oh.

**00:28:27 - 00:28:28**
You've been busy regarding our?

**00:28:28 - 00:29:36**
Sorry, I said, you've been busy, yeah. Regarding our bill, we require the NAV expert extrapolation data UH from NAV to be returned to the Diverse. And adjust the volumes in the respective Our bill. If Diverse does not update the respective Our Bill that has extrapolation data, then the volumes will be out of sync. Does that make sense? Yeah, okay, okay, so it's right in there. TC08, Okay. I actually thought when I added it to TC07 that it would fall under TC06, but it doesn't.

**00:29:38 - 00:29:45**
Oh, that's TC07, the mobile thing. Yeah, so I did submit that to support.

**00:29:46 - 00:29:48**
Yeah, that is so weird.

**00:29:49 - 00:29:55**
Yeah, I mean, I saw it happen real time, so you're not crazy. You're not making it up.

**00:29:58 - 00:30:30**
At this point, we'll just go with the extrapolation data as our critical item. Because I honestly think by the end of April, all these other identified critical items are not critical. Right. Because we always circle back to the extrapolation data. Always. Yeah. Well, the column's not there. Right. The column's not there. Well, the columns aren't there. Yeah, okay. Do you need that column? Is that column important on the Arab bill?

**00:30:31 - 00:30:49**
I think that's what was getting missed was, like, from David's perspective and ABCRC's, from what I understand, it's super critical. The way Mark understood it was it's just associated with a report. And since you're already producing that report, why do you have to push it back to us?

**00:30:50 - 00:30:51**
Exactly.

**00:30:51 - 00:30:56**
That's where it got lost is it was surface level and it wasn't deep enough.

**00:30:57 - 00:31:19**
Right. Mark's thinking it's a report. David is viewing it as critical, critical volume data. Yeah. And that's the piece that nobody caught on. Yeah. Wait a minute, because everybody kept looking at the report without actually seeing the report. And that was the difference. Yeah.

**00:31:20 - 00:32:08**
So if that's the case, then, you know, I.I think I personally have a better understanding of David's frustration. Yeah. Because the U.S. surfaced that David feels like he's not being listened to. And so if he's brought this up, and again, I don't know all of the history. I only know the last bunch of months. But if he's brought this up multiple times and it's been just kind of squished down every time, then of course he's frustrated. So let's see if we can remove that. That's my plan tomorrow is to say, but I did tell them that I want to meet with you guys to talk about all of the missing stuff that has been identified by ABCRC so that we can figure out how we move forward.

**00:32:09 - 00:32:24**
So that's why I was in a bit of a panic to get that itemized list. So if it's just the one thing that's... If it's not, let me know by the end of the day, just so I can listen. Yeah.

**00:32:28 - 00:32:29**
Yeah.

**00:32:48 - 00:32:51**
Showstopper is the extrapolation data.

**00:32:51 - 00:33:14**
Okay, got it okay, I can work with that. Okay, all right. Well, thank you sir, and by the way, thank you for your support in the training. I think we made a good team, so hopefully they have the team, you know, is happy with what they received. And like, I said that, that's the first time that this type of training has been delivered to anyone. So, yeah.

**00:33:14 - 00:33:21**
Oh, you have item that you haven't done. And today's Tuesday I have an assignment.

**00:33:21 - 00:33:22**
What's my assignment?

**00:33:22 - 00:33:34**
Well, we, it deals with training, so we did set up, yep, where's your operate? Where's your operational training document? Did it go through for you?

**00:33:34 - 00:34:16**
Yeah, no, I, I have to. I'm delinquent on that, I owe that to you. So the part of the reason I held off was because the, uh, the the UI's changing. And so I don't want to create a training document that doesn't represent what they're actually seeing in the system. I think that's just going to cause a problem. So I've been holding off on it a bit. So I need to revisit that probably tomorrow, and I'll put some work into it. And then I'm not going to include the stuff that we agreed not to include, like the QC stuff. We'll take care of that later because I know for sure the QC stuff, the interface is changing a lot. To make it much more user friendly. So it's it's changing for a good reason.

**00:34:16 - 00:34:46**
Um, and so we won't do that and the shipping, uh, inventory stuff, the, uh, that's changing too. So yeah, we'll take care of that afterwards. But yeah, I think I think we should be in pretty good shape and then. Because this is more about the how, exactly how do they do it. There's going to be a lot of questions because they're going to be in going to, they're going in and actually doing transactions and stuff. And so that stuff I won't be as familiar with. So Mohsen's going to have to help there.

**00:34:47 - 00:34:47**
All right.

**00:34:51 - 00:34:53**
Sir. Thank you for your time. I appreciate it.

**00:34:54 - 00:34:56**
Thank you. And we'll talk later.

**00:34:56 - 00:35:00**
Yeah, we'll talk tomorrow. Tomorrow? Yeah, Wednesday. Yeah.

**00:35:00 - 00:35:01**
Yeah, tomorrow.

**00:35:02 - 00:35:05**
Okay, cheers. Bye. Cheers, bye.

**00:37:26 - 00:44:39**
Okay. Hmm.
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="5ac8732772fff197">>>
</file>
assistant: Already have this one, so I did not re-process it.

Existing file:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-14 ABCRC Training Feedback and Software Requirements Discussion.md`

Send the next transcript.
user: [media attached: /home/duane/.openclaw/media/inbound/2026-04-08_Dav_Duane_ABCRC_API_Integration_and_Project_Chall---5db12c96-3b6b-4db9-b3ae-c3bff6589e27.md (text/markdown) | /home/duane/.openclaw/media/inbound/2026-04-08_Dav_Duane_ABCRC_API_Integration_and_Project_Chall---5db12c96-3b6b-4db9-b3ae-c3bff6589e27.md]
[Discord #alfred-main channel id:1478436599074258954 +10s Thu 2026-05-07 13:33 UTC] Leitchy (dl_70): <media:document> (1 file)

<file name="2026-04-08_Dav_Duane_ABCRC_API_Integration_and_Project_Chall---5db12c96-3b6b-4db9-b3ae-c3bff6589e27.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="453b42b26507e2ee">>>
Source: External
---
# 2026-04-08 Dav:Duane ABCRC API Integration and Project Challenges
Creation Time: 2026/04/08 11:29


## Transcription

**00:00:00 - 00:00:03**
Good morning, Dav. Hey, how are you?

**00:00:04 - 00:00:05**
Doing well. How are you doing?

**00:00:06 - 00:00:16**
I'm okay. I'm just opening up a blind. It took me forever to get here. There was an accident on Deerfoot, so it took me a lot longer to get here.

**00:00:17 - 00:00:18**
Wow. Yeah. Was it a bad accident?

**00:00:21 - 00:00:25**
Not really. Just it tied up everything, right?

**00:00:25 - 00:00:29**
Right. That's good. At least it wasn't a fatality.

**00:00:31 - 00:00:37**
Oh, that I don't know. Once Deerfoot has one single accident, that's it. Things are doped, right?

**00:00:38 - 00:00:41**
Yeah, it's a pretty busy highway.

**00:00:44 - 00:00:51**
Yeah, well, it's going to get worse because they're looking at putting tolls on Stoney Trail so that they can pay for art installations.

**00:00:53 - 00:00:54**
Art installations.

**00:00:55 - 00:00:59**
Deerfoot's going to get really, really...

**00:01:02 - 00:01:03**
Nasty. Interesting.

**00:01:07 - 00:01:13**
Okay. You saw the emails going back and forth from Sam? I did.

**00:01:13 - 00:01:13**
Yes.

**00:01:25 - 00:02:37**
So I never had an opportunity. So you sent out the status. You mean Wednesday? Yeah. You sent it out Thursday. So, no, I did not have any time to walk Sam or Shane through the status report before it went out. Okay? Yeah. Now, Sam asked me, did I agree to the status report? And I said, no, I actually didn't say I agreed with the status report. What I said was that from the vendor's perspective, okay? But a lot of questions have arisen, and one of the big things is APIs. Yes. Okay? Now, we've been talking about APIs for a long, long time because we've been trying to get our heads wrapped around it. Okay? And thank you for your email back. I think it was Monday. So there's like, I think there's like 88 separate APIs. Yes.

**00:02:37 - 00:02:38**
Yeah, something like that.

**00:02:39 - 00:03:44**
Yeah, we'll just use the number 88, right? The critical thing, Duane, was the R bill, the R bill information, right? That's what NAV needs. Yeah. In your email and in our conversation, I started. Getting the impression that we may only have to build one, well, actually it'll be two APIs, but one big API that would go to all of the endpoints to gather the various components of the R bill to transmit to NAV, that we didn't need a separate API to do the site information and all this, right? So I'm talking with our developers. Our API developers tomorrow to start getting our head wrapped around that. Because based on quotes we got, there's no way ABCRC can afford to build 88 separate APIS. It's like an eight hundred thousand dollar bill.

**00:03:44 - 00:04:26**
Yeah, no, no, nor should you need to. Yeah, that's the point, right? And and I don't know that it'll just be one. So so what I was trying to point out in my email is it really depends on. Like, APIS are basically function calls, right? So if the function is is, go to Diverses and go to this endpoint, this endpoint, so let's say endpoint A, B, C, D, and E, and once you open those doors, pull this information, right? So it's like going into a house and it's got a variety of rooms, and in each room you want to grab different stuff, put it in a box, and bring it back, right? So that's essentially what the function is. So it really comes down to what are your use cases. So one use case might be that...

**00:04:27 - 00:05:10**
I need to have a function call that goes to Diversys and pulls all of the information related to the R bill. That can be one API function. So that's a function call. It might be another one that you require that says, okay, I need to take information now from NAV and post it back to Diversys. So that's a different function call. So that's another API, right? So that's what I'm trying to get to is, like, you need to understand what your use cases are. What needs to move, from where and and what triggers it, etc. And then that determines how many APIS you need. So, and I don't know your business completely, but but I'm going to say like, you need a handful, right?

**00:05:10 - 00:06:00**
So this is what I was pushing back to mark for a year. Okay, that I was not understanding why we needed all of these APIS, and I kept saying we need the R Build data. And in our conversations, we went through the R bill. Let's forget about the QC component. Let's forget about that. But the various fields, for lack of a better term, in the diverse R bill would be all the data that would be required to be sent to NAV. And so that's when I started really scratching my head. And this is where we were having the conversation. You know, I have to build a site API to get the site information. Then I have to. But so. No. I have the meeting tomorrow with the developers and we're going to walk through it.

**00:06:00 - 00:06:20**
Right. I'm going to show them this. Our bill is everything we need to be transmitted to that or to NAV. OK. So. I haven't had that conversation with Sam yet because my executive meeting is at one o'clock today. So I'm going to be walking him through all that. Okay. Okay.

**00:06:20 - 00:06:20**
Yeah.

**00:06:21 - 00:06:51**
And this is in our meeting with Mark, right? We need to be able to send back the expert. I can't say the word all of a sudden. Extrapolation. There we go. Extrapolation data that NAV does and send it back to that R bill. And if you remember my question. If that R bill is locked, how does it get that data updated?

**00:06:52 - 00:06:52**
Right.

**00:06:53 - 00:07:54**
Right. And that's when we got on the communication that diverse doesn't communicate to anybody else. It simply goes to its endpoints with inside its own application and pulls data or puts data there. Right. So it doesn't send anything out, doesn't pull anything in. So, yeah, so this is. Much more clarity than what we've been getting for a year on how do we get data out of Diverse and how do we get data back into Diverse? Because Mark has stated numerous, numerous times that Diverse cannot accept the extrapolation data from NAV. And my argument back to Mark has always been, it doesn't matter if the number or the data has a dollar sign in it, it is simple data, right? And Mark kept throwing back, we don't do any financial data.

**00:07:54 - 00:07:54**
Right.

**00:07:55 - 00:07:57**
We're not asking...

**00:07:57 - 00:08:00**
Yeah, sorry. I didn't mean to cut you off. Go ahead.

**00:08:02 - 00:09:08**
We're not asking you guys to do any financial calculations or anything, but these things have to show that financial data, right? So it's... My argument back is that it is simply data, whether it has a dollar sign, a pound sign or a hippo. It's just data. So why can't you guys accept that? And Mark's argument has always been, no, we don't touch financial data. But if data is data. It doesn't make sense. OK, so this is what this is sort of what Sam's trying to get to. Not understanding why. Diverse can't accept data regardless of what it is or what you want to classify it. Why can't diverse accept the data? Because they need that data, the extrapolation data, in the R bill. The other area that, based on what we got, is causing some confusion is the QC portion.

**00:09:12 - 00:10:33**
I've tried to push more records through the QC process. I pull up the transaction ID. It doesn't work. I can't remember. I've tried so many different things. Trying to get another transaction into the QC pipeline to switch it from target, target, or target random, or the three categories, right? And I can't seem to pull up any other transactions. And I don't know if it's a bug or whatnot, but I can't seem to pull it up. And so these are where the questions are coming from. Hold on. Here we go. I'm going to share my screen with you. This is multi-factor. By the way, I'm just on my laptop. So bear with me as I try to figure out which screen it is. Here we go. Okay. I sent you the screenshot. I have no idea why that's there.

**00:10:34 - 00:11:17**
No. I can only do email. I can't do send pets, even though my number is verified. Right. As I try to log in. Okay. Just one sec. Now I gotta wait for it. It does take a very in an email passcode, takes a lot longer than the text.

**00:11:17 - 00:11:28**
Yeah, it has to travel around the world. Yeah, I did get it working once.

**00:11:28 - 00:12:19**
I did get it working once, but, uh, with my phone. I just got the email. Two-factor authentication, right?

**00:12:20 - 00:12:21**
Okay.

**00:12:24 - 00:13:15**
Obviously, the last reset was performed yesterday. Okay. And I set it up to one day just because I'm trying to do various things, right? So, as you saw, I could only do email. And if we go to. The accounts. I'm going to do that. I used to. My number, if you looked at the screenshot, was verified. But each day I come in, the number is not verified. But the email remains verified. So if I click on verification.

**00:13:22 - 00:13:25**
Is that because it's set? Is it still set to one day?

**00:13:25 - 00:13:32**
Yeah, but even if I have it like longer periods.

**00:13:32 - 00:13:33**
Still the same.

**00:13:34 - 00:14:19**
Still does the same. So there we go. So I'm confirming it, right? And then I get the verification. But even when I set the security for more than one day, right, my number doesn't seem to stay verified. So if I do two days here, also, allowed me to do this. Oh, I guess if I change that to that.

**00:14:23 - 00:14:24**
Okay.

**00:14:25 - 00:15:39**
There we go. So yeah, so the little hiccup I'm seeing is my phone number loses its verification. So the curiosity question I have is the fact that for every verification we have to do, it's not going to accept the phone number. So it'll have to be by email because it takes the email address, says it's been verified, and saves it. Phone numbers, though, are not. So if we try to get people to use their phones as the multi-factor, When they have to re-authenticate, they have to use their email. So I'm not sure if it's a bug in here or whatnot, but my argument is once I verify a phone number, it should be treated like the email and be permanent verified until I come in here and change the phone number.

**00:15:39 - 00:15:53**
Yeah. When you do this, Dab, did you hit save just out of curiosity? Oh, yeah. Okay. Yeah, it should work. I mean, they're giving you a phone number, and the option is to receive a text. So, I mean, the functionality is there.

**00:15:54 - 00:15:56**
See, I saved it, and it's now verified.

**00:15:57 - 00:16:01**
Yeah. Okay. So I'll create a ticket for that.

**00:16:02 - 00:16:02**
Okay.

**00:16:04 - 00:16:28**
Yeah. Yeah, if you could help me with the ticket, Dad, by doing screenshots of that. I know you sent me some already, but if there's any additional that you can add or that you think makes sense, then send those along too. Otherwise, I'll recheck what you send, and if that's good enough, then that's what I'll use.

**00:16:29 - 00:16:37**
Yeah, because I don't know what else you need, because essentially the screenshots of the verification and whatnot. So, yeah.

**00:16:41 - 00:16:55**
Yeah, I'll create a ticket for that, no problem. Because you're right, it should work. It gives you the option to receive a text or an email. So if it allows you to put your phone number in and then validates it, verifies it, then you should receive a text.

**00:17:00 - 00:17:44**
Yeah, so you got the email screenshot. And then I said, yeah, I forgot the other two. I accidentally hit send before I added it. Yeah, the number was verified. I showed you the transaction history. So actually, hold on a second, because there we go. You don't have the one where I'm no longer verified. So just let me capture that and send that over to you. I like your question. Did you click save? Of course I did.

**00:17:45 - 00:17:46**
I ain't going to ask.

**00:18:24 - 00:18:26**
That's a big screenshot. There you go.

**00:18:38 - 00:19:51**
So based, okay, next topic is based on the conversations about meeting with the status reports. You know, we were talking about the executive meetings, and I had a brief conversation with Shane about that. The problem we have is April, May are two months, because I actually asked Shane, can you find any available time with you and Sam in the next six weeks? And he has yet to be able to come up with anything. He can't come up with anything in April. He's actually looking in May and trying to find this time. So that's why I was suggesting September because supposedly September is when things get lighter for them again. But now with the exchange going back and forth, they're seeing what they can do to free up the time because I said it's mandatory for both of them to be in that meeting.

**00:19:52 - 00:20:05**
Not just Sam, not just Shane. But if we're doing an executive project status meeting, both of them have to be in there. OK, so they are looking at the calendars trying to figure out what they can free up.

**00:20:06 - 00:20:49**
I think it's important to have the discussion because from from. Sam's understanding, like, we decided that it would, a high level is what Roger wanted. He wanted a high-level executive summary, basically, or status of the project, which is what we sent. Sounds like Sam wants slightly more granularity. So, like, we focused on, like, what are the key risks at this point in the project? So right now what we're looking at, what are those key risks? Because as you know, if we look in our risks register, there's like a half a dozen or there's a dozen or more.

**00:20:49 - 00:20:50**
Right?

**00:20:50 - 00:21:41**
So it didn't basically cut and paste everything out of monday.com into a presentation. I don't think anyone would appreciate that. But if he does want more, instead of having like an executive status review, that we have maybe a more granular. Project status review like, and we go through, like the action items and the risks and talk about those things. Instead of having it like a, it was essentially it was a stoplight presentation, right? This is green, this yellow, this is red. Maybe that's not what he wants, right? So that's what that's. That's what Roger asked to be presented, which is why it was presented that way. So he wanted an executive review of it. Um, Sam, it sounds like Sam wants a more detailed review. So I think we just need to land on what do you guys want?

**00:21:41 - 00:21:51**
Like what format is most beneficial to you guys? And then I can work on that format and how it best represents both companies.

**00:21:53 - 00:22:06**
Right. So the funny thing was even Shane was scratching his head about that because we have a detail weekly project status meeting. Okay. And that's where the details are. Right.

**00:22:07 - 00:22:10**
So it seems like Sam doesn't know the details, maybe.

**00:22:12 - 00:22:36**
Well, he does and he does and he doesn't. So his response had me scratching my head, to be honest with you, because we go in the details every Wednesday. So, oh, yeah, that's the other thing. You didn't add Sam and Shane to Monday.com. They can't see it.

**00:22:36 - 00:22:47**
Okay, I can do that. I was leaving. I didn't want to do that without you saying so because I knew you were presenting this stuff to them at your exact meeting. But I'm happy to do that. That's easy.

**00:22:48 - 00:23:11**
Yeah, give them access. It makes no sense to me for them not to have the access. But, yeah, give them the access. So, yeah, so it's scratching my head because before we agreed upon what's in monday.com, I was using my Excel spreadsheets for everything that's in monday.com anyways, right?

**00:23:11 - 00:23:12**
Right, yeah.

**00:23:12 - 00:23:25**
So today would be my first meeting with them going through monday.com as opposed to my regular Excel spreadsheet. Right, okay.

**00:23:27 - 00:24:01**
Sorry, part of the reason I didn't want to do that without you being involved in that decision, Dav, was because this is relatively new, like the monday.com action register and stuff. So if you look at the action register, there's still a lot of outstanding dates that need to be put in there that you and I actually haven't had a real good chance to go through and plug those dates in. So I didn't want to throw you under the bus and they say, well, Dav, you've got all kinds of actions here and none of them have closed dates. Going on so right, so I'm trying to be respectful of not throwing you under the bus.

**00:24:01 - 00:24:16**
Yeah, and that's perfectly acceptable. Um, as you see, I started, uh, trying to do some updates in there. Um, so yeah, so not worried about that at all.

**00:24:16 - 00:24:28**
Okay, so I'm adding them right now, just so, you know, okay. So I added them to the actions. I just added them to the risks, and I will add them to the decisions box now.

**00:24:34 - 00:24:41**
It's kind of funny. We get used to using more than one monitor. To be stuck on a single monitor is annoying.

**00:24:43 - 00:24:50**
Yeah, I agree. All right, so that's done. Taking care of.

**00:24:50 - 00:25:20**
Oh. Yeah, just a piece of feedback for you. So I had my camera working, right? Remember that? Yeah. And it's not working. So I got my Zebra, and the rendering of the login screen is vastly different than the rendering on my Android phone.

**00:25:23 - 00:25:24**
Okay.

**00:25:24 - 00:25:25**
Which is actually a good thing.

**00:25:26 - 00:25:27**
Okay.

**00:25:29 - 00:25:31**
That's not where I thought this was going.

**00:25:32 - 00:25:46**
Yeah. So remember when I did the screenshots where the word email and password were, like, in the middle of where you put your email and password? It is not on the Zebra device. Right.

**00:25:48 - 00:25:49**
Okay, that's good.

**00:25:50 - 00:26:16**
So, yeah. I mean, I don't think we're really going to have anybody... Yeah, I've got to figure that out. I don't think we'll have anybody really using their Android phone, but I'm not 100% sure on that. I'm also trying to...

**00:26:26 - 00:27:13**
Yeah, so I want to circle back to something we were just talking about. So you were talking about the extrapolation information, basically putting information back into Diversys. So if you remember the email I sent quite a while ago, that this is the requirement and we just need to do it, and Mark was challenging that, saying why do we need to do it? It's already being done. This is specific to the ASR report, by the way. He was saying that, you know, it's already being done by NAV, et cetera. And then his feedback was essentially that the reason we can't take the data back is there's nowhere, there's no fields to receive the data into. And those fields, they don't exist within the framework of the SAS product right now.

**00:27:14 - 00:28:01**
So essentially it would be a bolt-on or a customization of the software. So that was his feedback. And if you remember, I think that meeting was February 4th. And Sam said, okay, well, we need to take this away and have an internal discussion. So I guess we're waiting on what the result of that internal discussion was. So if it's absolutely mandatory and it has to be in diverseness, I think that needs to be raised. And then the team needs to come back to the table and basically fight it out. If, if it's justified, and then, like, because I don't know if Mark is going to say this is three months or six months of work to do this. Or if the company, if, if they handed them, are just going to say absolutely not.

**00:28:01 - 00:28:39**
It's not within our the framework of the software that I don't know that they will have. I'm not saying they will, I'm just saying we need to sort that out. And we haven't gotten there yet. So I respect what Sam is saying is like this is still a risk, and it is. He's not wrong. But we need to understand if the ABCRC team is saying absolutely it needs to be in diverses, there is no ifs, ands, or buts, that has to work that way and here's why, then that needs to be presented back to our team. And I think that's what we were waiting on.

**00:28:41 - 00:29:56**
Right. And here's the catch to that. Since day one, ABCRC has consistently said that that was critical for success. It was part of the critical success criteria. And so that's why they're a little bit confused why it's not there. Also, the fact that, yes, I did understand what Mark said. Came back and stated, What you just did, that it's not part of your framework. The catch is that for ABCRC, for that information not to be in there, the application is useless to them. They might as well stay with NAV, however. Me saying that, and I had a brief conversation with Shane about this. We will need to set up, and I told him I need it sooner than later, the four of us, me, five of us, me, you, Roger, Shane, and Sam have to be in a room where the official decision is yay or nay to that.

**00:29:57 - 00:30:39**
Okay? Because I do remember, oh, it's been well over a year that. Both Sam and David kept saying to Mark and to Molson that they needed that information in diverse. The pushback we kept getting was it's financial data. We don't do financial data. And the big argument was this was just data. So that requirement has been there for a long time. And somehow it's gotten really muddied and whatnot. So, yeah, we need to have a critical meeting.

**00:30:40 - 00:30:42**
We need to iron that out.

**00:30:43 - 00:30:43**
Yeah.

**00:30:45 - 00:31:18**
Sorry, I got looped into it on the February 4th meeting, right, where David was basically demanding this. And so the history, I wouldn't know. If it was done a year ago, I wouldn't know that. But I do know right now that it's critical that a decision be made on that one way or the other, right? And so both teams, both sides, and I don't want it to seem like it's adversarial, but the team as a whole needs to decide one way or the other what direction we're moving in. Right now we're basically at a standstill.

**00:31:19 - 00:31:32**
Yeah. But that's why I'm saying the five of us, not to have Mark in there, not to have David in there, the executives. Basically, Roger and Shane have to make the executive decisions, right?

**00:31:32 - 00:31:47**
Yeah, unfortunately, Mark needs to be there because he's the VP of product, so he's the decision maker on whether it goes in or doesn't go in. And so he's the only one that can basically speak to why, why or why not.

**00:31:48 - 00:31:51**
Right. Okay, so I didn't realize that that was his title.

**00:31:51 - 00:31:57**
Yeah, he owns product, so he makes the decisions on what goes in and what doesn't go in.

**00:31:58 - 00:32:10**
Okay. Yeah, because this is critical because... You know, just between you and I, if that's not in there, then there's no sense in us continuing with the product. It won't work for them.

**00:32:11 - 00:32:36**
Yeah. And I mean, if that's the position, then my recommendation would be come to the table with the why, why that is. Because Roger's not going to understand it, right? So there needs to be a high-level overview of, you know, this is the request. This is why it's the request. This is why it has to be there. This is why it's fundamental. And then Mark will have to say that, yes, I agree or no, he doesn't agree, and here's why.

**00:32:37 - 00:32:40**
Yeah, so that's going to come from Sam and Shane, right?

**00:32:42 - 00:33:27**
Yeah, whoever it comes from. I don't know who's going to have the details on their side, but, yeah, whoever. It's just that's the information they're going to need to know instead of, you know, this is what we desire, and the pushback is, well, we're not sure why you think you desire that or need that, and here's the reasons why we can't do it or won't do it. And I'm not saying they won't, by the way. I'm just saying that they need to know that this is the absolute why. It's a deal breaker. You know, if it is, in fact, a deal breaker. Because if you remember specific to the ASR report stuff, Mark was saying, but it's already being done in NAV. So why do you need to push it back into Diversys?

**00:33:28 - 00:33:40**
And then Taz spoke up and said, yeah, well, actually, we need it in NAV so we don't have to go to the two locations. And then I know that changed as the conversation went on a bit, but it seemed to be there was some cloudiness around the reason why.

**00:33:42 - 00:34:00**
So the criticality was using one app. One application over two. And the argument that came back out of that particular meeting was, well, if we're doing everything in that, why are we using diverse, right? So that's when we come into this catch 22. So yeah, we need to get.

**00:34:00 - 00:34:03**
We need to make a decision.

**00:34:03 - 00:34:12**
Sam, Shane, Mark and Roger in a room, they have to come up with a decision. And then based on that decision, Sam and Shane have to make their decision.

**00:34:13 - 00:35:11**
Yep. Yeah, 100, because I mean, I I appreciate where Sam is coming from, I, I do, you know, um, and and I think, like, well, one of the challenges that I.I'm not sure I understand correctly. Because he was saying, like, you've got N Corp data in an ABCRC presentation, but it's not specific to N Corp. It's it's specific to the product. The fact that ABCRC is not using it is irrelevant, really. Because you could use it. That's a choice. ABCRC is choosing not to use it. But anyway, that's neither here nor there, I think. But some of his other points are valid, right? That, you know, there is the stuff. Like he talked about the random random and the target random and stuff like that. So that is there, right? As you know, you saw the presentation on that. So I think he was unclear on the details about that stuff. Hold on.

**00:35:11 - 00:35:52**
Hold on right there. Sorry. Got to stop you right there. Molson showed us it, but I have yet been able to get it to work. So that's where I haven't been able to come back and said, yes, Sam, it is there because I can't get it to work. I can't get anything else in the QC pipeline. At this point, you're saying it's there, and yet I'm saying it's not because I can't get anything into the pipeline to change it to any of the three categories. Okay? Right.

**00:35:52 - 00:36:07**
I think those are two different things, though, Dave. Be honest, because, like Mosin demoed it in your environment, showing it working so so it, I think we can agree. It's there. Whether it's fully functional is, it's another look.

**00:36:07 - 00:36:50**
So that training went very fast. Okay, all right, and this is why I'm not agreeing with you is if. We have one item in the pipeline, okay? Just one second. So we have just these items, which is what Molson did, right?

**00:36:50 - 00:36:51**
Yep.

**00:36:51 - 00:37:55**
These three. Oh, sorry. Okay? But I can't get anything into the pipeline to try anything else. The other thing is there's no record here that tells me which one this was. Let's exit. Okay. So there's the transaction ID. This is the audit result, but where was the identification of what it was? Now, where's the document? Hold on. Can you still see my... Your screen?

**00:37:56 - 00:37:56**
Yeah.

**00:37:57 - 00:38:00**
Okay, so you see that I have your diverse training document out, right?

**00:38:01 - 00:38:02**
No, I just see the diverses screen.

**00:38:04 - 00:38:12**
Jesus. So the training document you gave me was just for setup, right?

**00:38:12 - 00:38:13**
Yeah, correct, yeah.

**00:38:14 - 00:38:23**
Okay. So from an operational perspective, I can't replicate what Molson did.

**00:38:24 - 00:38:24**
Right.

**00:38:25 - 00:39:21**
Yeah, so I'm not saying we don't need to focus on training and so on. That's a fact. I'm also not saying that it's fully functional. I mean, I know it's there. The functionality is there. It's in the software. Like Mohsen demoed it. Whether you've been trained on it properly or not, the fact is I think we can agree, no, you haven't been, nor has your team. Is there additional functionality that needs to be built into QC? Yes, I would suggest there is. But I don't want to set the impression that random, random, target random, and I forget the other one, that they haven't been accounted for in the software. And that's where I'm coming from is I think Sam's message was basically that that stuff has been identified as a need for ABCRC and we haven't addressed any of it. And I don't think that's the case.

**00:39:22 - 00:39:33**
Well, okay. You say it's in the software, right? You say that Molson demoed it, correct?

**00:39:33 - 00:39:33**
Correct.

**00:39:34 - 00:39:39**
So from Diverse's perspective, it's in there, right?

**00:39:41 - 00:39:42**
If I go in.

**00:39:42 - 00:39:43**
Sorry?

**00:39:44 - 00:39:48**
Yeah, the requirement for those items have been accounted for in the software.

**00:39:48 - 00:39:59**
Yes. If I can't go in and replicate the three categories, how can I agree with you that it's in there?

**00:40:00 - 00:40:46**
I don't want to split hairs and argue it, but it's functionally. It doesn't work functionally versus there. I think it might be two different things. Have you been trained on it? And I'll give you another example. So we were just talking about 2FA, right? So we agree that two-factor authentication is in the software. You're saying that it might not be working properly. Those are two different things. I don't think you're telling me that we don't support two-factor authentication. You're just saying that there might be a bug with it. Right. So I'm suggesting the same thing. It's in the software. Does it work the way it needs to work? Are you able to test it and verify it? Maybe not. And I think that's where we need to say, yes, it's there. I haven't been able to validate that it's fully functional yet.

**00:40:49 - 00:40:51**
You're trying to get me to sign off on an application.

**00:40:52 - 00:41:15**
No, I'm not asking you to sign off on it. I'm just saying that Sam is saying it hasn't been accounted for, and I'm saying it has been. We've thought about it. We put it in the software. Does it need changes? Possibly. Then that's what's going to come out of the training feedback and stuff. So I'm not asking you to sign off and say that, yes, it's 100% validated and complete. What I'm saying is it's in the software.

**00:41:19 - 00:42:12**
Right. You're saying it's in the software and I'm saying I can't see it in the software. That's what I'm trying to say. So if I can't see it. And you're saying it's in there, but I can't see it. The same position, Sam, saying, look, we tell you that we need this in here and you're saying it's in there. And we're saying, well, we can't validate that it's in there. That's what we're trying to say. Because it's the same thing with this stupid supply inventory module where Mark gave me shit in that meeting that day that says, oh, we had so many requirement gatherings for this. Not once did Mark sit down with the team to find out what the requirements are. All of a sudden, we get a software release that changed what we thought would be happening.

**00:42:16 - 00:42:22**
Diverse can say everything's in there, 100%. Yes. You can say the C bill's in there at this point.

**00:42:22 - 00:42:25**
Sure. That's not. I can tell you that's not in there.

**00:42:26 - 00:42:52**
But if we can't validate that, yes, it's there. See, the problem is I can't validate that it's there. I can only validate one QC item is there, not the three. So, yes, diverse can say that everything's there. Fine. But if your customer can't validate it's there to the customer, it's not there. That's what the argument is.

**00:42:52 - 00:43:01**
You need training on it, for sure. I mean, it was demoed, but you haven't received what I would refer to as proper training on it.

**00:43:02 - 00:43:35**
Right. So I haven't been able to validate that the three QC categories, or whatever you want to call them, are there. And that's what he's saying. The other hitch about all this is what I call the partial releases. And it was a risk that I identified that if we are getting releases that don't have the complete workflow in, it is going to raise concerns to your clients.

**00:43:35 - 00:43:36**
Yep.

**00:43:37 - 00:43:37**
Right.

**00:43:37 - 00:43:39**
With us, too, by the way.

**00:43:40 - 00:44:22**
Yeah. But this isn't working. It's not there. And so that's where we're at. And I have said to Sam and Shane and the team itself that, look, we are getting pieces of it. It's not 100%. We are having some pieces that are released, right? This is why we're going into the training. There's enough there with the caveat that it's not all there to get the team to. To start working inside of it, right? That's why I got the POR portion, okay?

**00:44:22 - 00:44:24**
To become familiar with it, yeah, absolutely.

**00:44:25 - 00:44:26**
Okay.

**00:44:27 - 00:44:43**
And by the way, the release that just came out, I did check. It doesn't affect the setup part of the training. It affects the usability piece, which is like the next part, but it doesn't affect our setup training.

**00:44:52 - 00:45:25**
Little bit of feedback for you on the mobile app before I forget. Um, so I installed the Diverse app before the new release of the app. Okay, the only notification so the app doesn't tell me it needs an update until I need, until I try to log in. Are you aware of that? I was not aware of that.

**00:45:26 - 00:45:26**
No.

**00:45:27 - 00:46:06**
Okay. So when I start the app, it doesn't tell me that there's an update required. It's only after I log in and everything, click sign in, that it tells me, oh, an update needs to be done. And then, of course, I go through the update process. I've done it on one of my scanners, not both. So I do the update, and then I have to log in again. So I'm kind of curious why we would not receive a message prior to logging in that the app needs an update.

**00:46:09 - 00:46:16**
Yeah, I can ask, but I think that's pretty typical of apps, is you need to log in before it tells you that there's a new version.

**00:46:19 - 00:46:36**
On the phone, if I click on my apps, it tells me before I go any further, I just click on it. It says there's an update available for this app or an update is required even before I get into the app.

**00:46:36 - 00:46:44**
Yeah, I can check that. Maybe they'll tell me it's by design. I don't know. But I can ask. Yeah, I don't mind asking.

**00:46:46 - 00:46:56**
Yeah, I'll need to put that caveat into the training document. You know what I'm going to do?

**00:46:56 - 00:47:20**
And just to follow up on your previous comment about the partial release stuff, yeah, it affects my team too. I mean, we're trying to learn the software, and it's only partway there, so we can't test it. We can't play around with it. Can't get into it in in the depth so we can actually learn all the functionality. So, yeah, I, I, I understand, appreciate where you're coming from.

**00:47:20 - 00:47:30**
I'm going to send you two screenshots. I'm going to attempt to send you two screenshots.

**00:47:30 - 00:47:46**
I'm not sure if you saw a message this morning from me. Dev Uh, in ABC, the ABCRC action register, so the Uh. Remember we were talking about the update to the API specs, so the table that Mark was talking about to make things a bit clearer.

**00:47:46 - 00:47:48**
Oh yes, yeah.

**00:47:48 - 00:47:58**
So that's there now. So I attached it in to the action item in UH, in the action register. You should have received an email about it. If you didn't. Okay, you got it.

**00:47:58 - 00:48:07**
No, no, and I actually have it up, but uh, do I have the wrong one up? Yeah, because is it sick. Hold on, I've got to check my numbers here.

**00:48:08 - 00:48:08**
It's 17.

**00:48:11 - 00:48:14**
That's 16 I don't want. That's 15 I don't want.

**00:48:14 - 00:48:15**
106.

**00:48:17 - 00:48:18**
It's version 17.

**00:48:20 - 00:48:23**
Yeah, it's version 17. They updated the version.

**00:48:23 - 00:48:34**
Yeah. So, yeah, I did see that. I downloaded it to take a look at it. Yeah, I didn't get a time to actually look at it.

**00:48:34 - 00:49:09**
I think Mark put in the, and I put it in the comments, I think it's page 219, I want to say. Let me just pull it up real quick and I'll tell you. Yeah, 219, see page 219. I knew you were going into your discussions with your API vendor. So I wanted to make sure that I got that to you. So I just received the first thing this morning. So I sent it first thing this morning.

**00:49:10 - 00:49:10**
Yeah.

**00:49:12 - 00:49:18**
Yeah, I see it now. But, yeah, I'll take a look at this later on today.

**00:49:36 - 00:49:40**
I haven't even looked at it, so I don't even know what that looks like.

**00:49:41 - 00:50:33**
Just one second. That's a much better document. I'm looking at 219. Yeah, good. Get transaction details.

**00:50:44 - 00:51:21**
Yeah, so hopefully with that information, plus the information, the back and forth that you had, you and I had that provides a bit of clarification because even in Sam's message, he was talking about the nine APIs and what he's referring to is API endpoints, which are similar but not the same thing. So you maybe don't need nine APIs. It really depends on your use cases and the function calls you need. So is that one? Is it 21? We don't know. Right. That's what needs to be figured out.

**00:51:24 - 00:51:46**
Okay. So without going into detail, just at a very high level, but yes, this looks like there's more, a lot more information that we require to make more sense of the APIs. So, yeah, I mean, just quickly going through there, what I was asking about in our previous meetings is being answered here.

**00:51:48 - 00:52:35**
Yeah, I knew that's what you were missing, which is why when you and I had our meeting last week, I'd gone ahead and just done that unofficial table to sort of give you some indication of, like, it's not all in one spot. It's in multiple different endpoints. You don't need multiple. You don't need an API equivalent for every API endpoint. That's not the way it works. I know that caused some grief back a little while ago. If you remember Shane's message saying, oh, my God, we've got to do like 90 APIs at $5,000 a piece, that's like $450,000. I was like, no, no, no. No, you don't need to do all that.

**00:52:36 - 00:52:39**
But we were going based on your documentation, right?

**00:52:39 - 00:52:49**
Well, probably the documentation and past calls that you maybe had. Where maybe enough clarity wasn't provided around the way it works.

**00:52:50 - 00:53:32**
Well, yeah, we kept asking for clarity, and, yeah, we just weren't getting the answer. Mark's a tech head, just like David is, and they get into their head on a technical level and have difficulty coming out to the non-technical levels. But basically, on the first blush of that document, this is what I was asking. From Mark for the past two years, right? So I've been on this project since 2024, and that's what we've been asking for, especially when the APIs first came out. So, yeah, it's making a lot more sense.

**00:53:33 - 00:53:46**
Yeah, because I think the first version of the APIs, and correct me if I'm wrong, was June of 2025. Is that right? May or June of 2025?

**00:53:47 - 00:53:50**
Something like that. Like, yeah, a long time ago, yeah.

**00:53:51 - 00:54:01**
2017 or something, right, was when they did the API endpoints? Somewhere in that range, I think. It was before I started anyway. But I think it was only like a few months before I started.

**00:54:03 - 00:54:48**
I can't remember when we got it. But, yeah, it started raising more questions than answers, and we were trying to get an understanding. With Mark and David at complete odds, you know, internally here, I was having a hard problem. And I just got the authority last week or so to engage open source to start asking them the questions about the API. So yeah, this, this I definitely will send over to open source for our meeting. And yeah, if we want to have to build one or two, even five APIs, that's a lot different than that in the build 88, right?

**00:54:49 - 00:55:09**
Yeah, yeah, absolutely. Yeah, I think that should bring the temperature down a little bit, hopefully, with some clarity, and hopefully the information I've been feeding you is helpful as well. I saw your email right away. Our company was closed on Monday, but I saw your email, and I know the importance, so that's why I worked Monday to respond.

**00:55:11 - 00:55:12**
Oh, I thought you were working Monday.

**00:55:13 - 00:55:22**
No, we were off both Friday and Monday. But, I mean, I didn't have any plans anyway. So as soon as I saw your message, I'm like, you know, I recognize the importance.

**00:55:25 - 00:55:29**
Typical Ontarians, taking all the time off. Never working in the office.

**00:55:29 - 00:55:37**
Yeah, yeah. Actually, I work way more than I should. I'm often working weekends just to make sure I'm covering stuff off.

**00:55:41 - 00:55:59**
All right, so the auction item is for me to work with Sam and Shane to get them to free up their calendars so that we can have a five-person meeting in which Roger, Mark, Sam, and Shane can come to an agreement about the extrapolation data from NAV.

**00:56:00 - 00:56:22**
Yeah, and all parts that require that. So, like, make sure that they're including, like, if it's ASR's miscount or whatever it is, like, these are all the pieces that require that functionality. And I'm sure we don't miss anything and call it all out. So you would probably know that better than I do, but I know ASR is one part of it.

**00:56:23 - 00:56:57**
Yeah, there's quite a few different – I'm just going to use the – word report very loosely that requires that data. So it's not just a one-time use data, and that's what the catch is. But what I'm going to do is I'm going to work with Sam and Shane for them. So when we get this meeting, what I would like is for you and I to be flies on the wall, that both sides present their arguments to each other, and for them to come to an agreement. And then whatever that agreement is, is our marketing orders.

**00:56:57 - 00:57:32**
Yeah, yeah, I agree that I think that's it. And you're, you're spot on, like, I can't make the decision and not neither can you. So, right? They need to decide, like we collectively need to decide as a team, that this is our path forward, right? And and we agree and we march on. Because right now it's sitting in limbo and it's like, You know, ABCRC is saying we want this and this is why. And, you know, our product team is saying, no, we can't do that and this is why. And we still don't understand why it makes sense. And I think we need to get past that and make one decision and move on.

**00:57:33 - 00:57:44**
Okay, I'm going to have to let you go because I've got my next meeting and I've got to actually walk into the plant to do it. Okay. So, yeah.

**00:57:45 - 00:58:09**
One thing, if I can ask you, Dad, before you go, is if you get a chance, can you go and plug in as many close date or target dates in the action items as you can? I know you're not going to be able to do them all, but any that you do know or are comfortable with, that would help to sort of round this out before we have our meeting with Shane and Sam and them so that when they go in, they see that we're actually tracking something to a date. Yeah.

**00:58:10 - 00:58:12**
No, as you saw, I started doing that yesterday.

**00:58:14 - 00:58:19**
Yeah, if you have any questions with any of it, just, you know, I'm always available. Ping me.

**00:58:20 - 00:58:21**
You got it.

**00:58:21 - 00:58:23**
Okay. Cheers. Have a great day.

**00:58:24 - 00:58:25**
You too. Bye for now. Bye.

**00:58:29 - 00:58:29**
Bye.
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="453b42b26507e2ee">>>
</file>
assistant: Done.

Created:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-08 Dav Duane ABCRC API Integration and Project Challenges.md`

Send the next one.
user: [media attached: /home/duane/.openclaw/media/inbound/2026-04-07_Internal_ABCRC_Project_Management_and_Communicati---c64a7417-2cdc-47f4-8ae2-535e4cc7218b.md (text/markdown) | /home/duane/.openclaw/media/inbound/2026-04-07_Internal_ABCRC_Project_Management_and_Communicati---c64a7417-2cdc-47f4-8ae2-535e4cc7218b.md]
[Discord #alfred-main channel id:1478436599074258954 +10s Thu 2026-05-07 13:34 UTC] Leitchy (dl_70): <media:document> (1 file)

<file name="2026-04-07_Internal_ABCRC_Project_Management_and_Communicati---c64a7417-2cdc-47f4-8ae2-535e4cc7218b.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="c4be8793baca1e7f">>>
Source: External
---
# 2026-04-07 Internal ABCRC Project Management and Communication Alignment
Creation Time: 2026/04/07 10:01


## Transcription

**00:00:00 - 00:00:45**
Like, is Dav communicating to him on things? And two, actually, I liked Sam's note from the sense of we hit a nerve, right? Like, I think if we'd gone in and hadn't been specific, he wouldn't have responded. But I think we were clear enough that it irked him to say, okay, this project's off the rails a little bit from their side, and they don't want to take ownership for it. So I think we got their attention. I still find it shockingly unprofessional by these folks that they don't want to jump on a call and everything is done over email. Right. Like when I get in front of them, they just clamp up and then they send like long winded notes that you saw this. Right. Basically, I just toss it into Copa and said, summarize this.

**00:00:48 - 00:01:30**
It's spot on because the original proposal was to. For this meeting, like for this presentation, was to have a meeting about it and they they declined. And then I put that in, and when I sent it, I.I made the offer again, saying, if you want to jump on a call, we're happy to do that. And they still haven't taken us up on that. I followed up with Dav yesterday saying, hey, I just wanted to touch base with you on Sam's feedback. I'm just curious to know, did Sam come and talk to you before he sent his feedback? Because I said to him, you and I have covered all of these things that are in his email. We have a risk register. We've talked about the outstanding decisions that need to be made, et cetera.

**00:01:31 - 00:01:49**
So I said I'm a little surprised at some of his feedback. So DAV didn't respond yesterday, but he just responded a few minutes ago saying that, no, Sam didn't come and talk to him before sending his email. So that means two things. DAV is not communicating upwards, and they're not going to DAV for questions before they come after us.

**00:01:50 - 00:02:21**
And I think there's a third. I think it's DAV is, I mean, Sam and Shane pay DAV salary, right? And he's a contractor. So he's going to intrinsically. Toe their line, right? Um, so when he asks things, he'll he'll phrase it in a way that that aligns with the way Sam wants to think about things. He's not going to be, he's leaving it to us to to message it. So, um, hey Mark, um, hey guys.

**00:02:21 - 00:02:21**
Sorry.

**00:02:21 - 00:02:52**
Good, good, so yeah. So like I said, I just basically took his email, hit the words. And Coppola hit summarize. It spit out this document. So I don't have enough detail on this project to be able to find what it did right and wrong. But I liked its approach because it aligned with Sam wants us to fix everything. And we've got to address those points, right?

**00:02:53 - 00:03:08**
The stuff that you're looking at on the page right now, Roger, where you see where it's highlighted in yellow, it's basically, from what I can see, it's just basically broken up that one fact into three. So it's, from the nearer I can tell, that's the same thing. It's all the same thing. Yeah.

**00:03:08 - 00:03:26**
So can we, let's go through each one at a time. How many are there? There's 14 of them. I think a lot, like you said, half of them are just points. So when you say comments, comments, is that how you intend to respond to Sam or is that an internal comment?

**00:03:26 - 00:03:32**
No, that's just internal. Yeah, no, that's not a customer-facing response, no.

**00:03:32 - 00:04:01**
No, I didn't think so. I just wanted to make sure that we were there, right? So clarity on phasing, I think you're right. You just reiterate what was in the slide. So delayed feedback and unresolved decisions may still drive additional scope or future releases. Leave it at that. Clarify API scope and assumptions. Yes, exactly. That's why I read it right. Like they have our endpoints. They can go off and develop it. Right. So I think we just.

**00:04:04 - 00:04:47**
They have a fundamental misunderstanding. So even in Dav's message yesterday that he sent me. They believe that for every endpoint that Diversys has, that they have to develop an API. That's their belief. Yeah, still, even yesterday. And I said to Dav, I'm like, no, Dav, that's not the way it works. You can have one API call that goes in and touches, like, you know, 10 different API endpoints in our system, just pulling data from sites, from participants, whatever. You have to figure out what are your use cases, so how many bridges do you need to build between the two systems, and what data needs to come across each of those bridges.

**00:04:50 - 00:05:52**
It's just different people's definition of what an API or an endpoint is. Technically speaking, what we have is an endpoint. The API is a concept. So they can build, when they press a button, they can build a function that calls one endpoint or calls five endpoints. That's a function. What they're calling an API, not 100% clear what they mean. And I bet there's different definitions within ABCLC as to what an API really means. Is it one API? Is it nine APIs? What's important is how many endpoints they need to support on diverses. They may develop 20 different functions inside nano. That uses still nine endpoints because they might have a function that says update. They might have a function that says delete. They may have a function that says, you know, extract, pull.

**00:05:55 - 00:06:27**
That's a nav decision, right? So we can't dictate how many different API calls or functions they're going to build. Right. What we can say is, you know, You've got, you know, X, and number of endpoints that you're going to use, and the number of endpoints they're going to use. Yeah, I'd have to review it. Uh, I don't know where. Nine I'd like, I'd like to know what he believes the nine to be.

**00:06:27 - 00:06:32**
Yeah, that's what I was wondering, Did we align on a not on nine? I was wondering that at least that would have been progress.

**00:06:32 - 00:06:57**
Now. Where that comes from is Dab went through all of our API endpoints and said, Okay, I don't think we need to do this one. I don't think we need to do that one. So then he basically came back and said, okay, we think we only need to do the transaction endpoints. We only need to be worried about those. And so in their mind, if that's nine, they need to develop nine APIs that match to those nine transactional endpoints.

**00:06:58 - 00:06:59**
But why would that be nine?

**00:07:01 - 00:07:08**
I'm not sure. Remember he showed that list, Mark? He went through our endpoints and he highlighted, like there was nine items he highlighted?

**00:07:10 - 00:07:26**
No. That's what I'm struggling with. We have the events. Right. Yeah. But those events could be, you know, it doesn't map one-to-one onto endpoints.

**00:07:27 - 00:07:52**
Yeah, because he went through the, remember originally they were saying, oh, we have to develop 80 APIs and it's going to be $5,000 a piece. So, you know, it's $400,000 and so on, right? Then we went, but yeah, you don't need to do that. Maybe there's endpoints that you're not going to touch at all. And so then Dab went through and said, okay, I think we only need to do these ones. And that's where they're coming up with this nine is what I believe.

**00:07:54 - 00:08:35**
So two things. One, can we draw a visual – like if we just said – like let's give them a representation where it's just like you have a – you don't have to necessarily do it this way, but this is just off the top of my head. Like the Diversa software, you have API endpoints, like sort of – it shows sort of like the highway on ramp kind of thing. The actual highway is not built by us. Yeah, we've got that somewhere. Okay, can we pull that out again? Like if we've done that, let's pull that out and then resend it to them. And let's look at it to make sure it makes sense. Like if you could share that with me, I'll try and put like, it won't be difficult putting on like a layman's hat and see if I can make some suggestions.

**00:08:35 - 00:09:28**
Like I think if we've created that, I think we need to send it back and we can put up, I think we need to show them visually what an endpoint is and have at the bottom, define endpoint, define an API and who is responsibility to versus. Endpoints, we own these. We've given you the spec. We gave it to you like closing in on a year now. APIs, it is the responsibility of ABCRC to get a third party to develop those and leave it at that. But anyway, like if you could pull up that diagram that you've done, I wouldn't mind seeing it. I think we need to. Some explain to them, simplify, because in words, it's, it's, it's there. Um, okay, so if you could, you could fire that over, um, three, four, five.

**00:09:28 - 00:10:02**
The concern I have here immediately starts with I believe that was discussed, this was discussed, this was discussed. I hate the word this is discussed. It should be everything. The source of truth has to be. Monday. Com. It can't. I don't remember like, when people come to me and say, Roger, we discussed this a month ago. I have no record. Like, you can't expect people to remember this and walk away with the same understanding and everything. It's got to be in Monday.com, so I would reference this one for the next three. Are these actively tracked in Monday. Com.

**00:10:04 - 00:10:12**
So the reason it says I believe this was discussed and you'll see Mark's name there is because I'm not positive that it was. I think it was. I think that this I don't care.

**00:10:12 - 00:10:26**
I don't actually. It's irrelevant if it was or it wasn't. We really have to get past this point of I talked about it on a meeting. I sent an email. That is a horrible. We cannot. We cannot run projects this way. It has to be mundane.

**00:10:26 - 00:10:46**
We're not going to send the message, but I wanted to have it highlighted so we talk about it here so that I'm clear. Because I think that remember when we had our meeting with them in Alberta, Mark, that they were talking about this batch processing? And if I recall correctly, you said, yes, that's the way it works today, but we're working on live posting.

**00:10:48 - 00:11:09**
But what you're saying right there is proof that this process doesn't work because even you're not clear. So we can't expect the customer to be clear. This should have been, based on the meeting in January, an action in monday.com to build the plan or build the plan of the plan or the plan of the plan of the plan. Whatever the next steps are, it should be very, very clear.

**00:11:09 - 00:11:22**
I think the next steps have already been taken, though. That's my point, is I think it's already on the roadmap. And it's for delivery in phase four, I think.

**00:11:23 - 00:11:24**
Is it in monday.com?

**00:11:26 - 00:11:28**
This specific item? No.

**00:11:29 - 00:12:14**
This specific line item number three action, provide a committed resolution to live batch. So the action is to get to a resolution for live versus batch posting. That's the action. And then there's going to be a whole bunch of subtasks we need to do and they need to do to get to that resolution. But if we don't have a plan. To get to a committed resolution, this is not their fault, this is our fault. And so we have to, I can't say this enough, we have to get away from assuming we had a call, we had an email. If it's not in monday.com, it's not on the project. That's the way I'm mapping this. So do we have a way to get to the committed resolution for a live batch that's got steps?

**00:12:15 - 00:12:54**
Invite with owners in monday. Com. That we, and if we don't, we have to build this. And then we can go back to Shane and show him this is. Um, when we met together in the meeting in January, there was some act like there was going to be a subsequent meeting. I think in early Feb or whatever. Even I don't remember. But it needs to be in Monday.com, otherwise it's noise, it has to be in Monday.com, otherwise you're. You can't say to them, well, Shane, we spoke about this. I'll tell you this, nothing infuriates senior management more than saying, well, we spoke about it. Who cares? They need the plan. And so for three, four, and five.

**00:12:54 - 00:13:00**
We do have the action items, Roger, in monday.com. And in fact, I went back seven. Okay, can we bring them up?

**00:13:00 - 00:13:01**
Let's walk through them.

**00:13:01 - 00:13:07**
That's the purpose of this meeting. Then let's open it up. Let's see what the plan of record is for resolving live versus batch.

**00:13:07 - 00:13:23**
Yeah, I'm not sure that that's in there. That's my point. And so what I'm trying to explain is I went back seven months of meetings to build out the action register that didn't exist. It now exists. I reviewed it with DAB and said if there's anything missing, let me know because it wasn't in the meetings.

**00:13:24 - 00:13:26**
So we didn't know about live versus batch?

**00:13:27 - 00:13:28**
No, this might be one of those items, yeah.

**00:13:29 - 00:13:31**
So we didn't know about this item?

**00:13:31 - 00:13:34**
Well, I think we know about it. I just don't think it was captured as an action item.

**00:13:36 - 00:13:38**
So that's bad on us.

**00:13:38 - 00:13:43**
Yeah, so we need to capture it as an action item. And they didn't capture it as an action item either until now.

**00:13:44 - 00:13:48**
Doesn't matter. At the end of the day, when this implodes, the customer's not going to remember that it was their bad.

**00:13:49 - 00:13:57**
So I can add this. It's just the reason I put Mark's name is because he will know whether we're actually doing the live versus the batch or we're not.

**00:13:58 - 00:14:05**
I'm not looking for the answer to this. I mean, I obviously want to get to a resolution, but what's the steps that need to get to a resolution?

**00:14:06 - 00:14:19**
But if those steps have already been taken is the point, right? Maybe it's already in release four, and that's what I need to know. So when I put the action in there, I can say that it's the action or resolution is that it's being delivered in phase four.

**00:14:21 - 00:14:23**
What is being delivered, live or batch?

**00:14:24 - 00:14:32**
Batch is already there. Batch posting is there, and the requirement is for it to be live. So that's the question.

**00:14:32 - 00:15:04**
So, yeah. Injected myself because I do think it's more about the mechanics versus the actual response to this one. But yeah, we are. It is tentatively planned for phase four, but the reality is that we still have many questions. Or let's just say alignment around the around that integration. The last conversation we had on the integration, David said, build it this way, and we said, we don't build it your way.

**00:15:05 - 00:15:05**
Yeah, I remember that.

**00:15:06 - 00:15:14**
So we're tentatively pushing forwards with the assumption that what we're building is going to be what they use.

**00:15:15 - 00:15:35**
And that worries me because we shouldn't be tentatively assuming anything. We should be getting signed. This is what we're building. Sign off or don't sign off. If you sign off, wonderful. If you don't sign off, where's the gaps? Let's solution the gaps and come to an alignment, but that that is not going to work. It's it's. We just need to be kicking it down the can, like the can down the road. So well.

**00:15:35 - 00:15:41**
The key is we gotta. That's why we keep pushing for this integration conversation so we we can reach that alignment.

**00:15:41 - 00:16:04**
Yeah, so that's why we need to capture what needs to happen, like even it just needs we. Just. This just needs to be mapped into. Monday. Com with clear steps. When is the next meeting? Happen to discuss this? Yeah, provide a committed resolution for Live. Agreed. I agree with them. Yeah.

**00:16:04 - 00:16:15**
And again, uh, I have a slide deck that we presented this all to them, including the mechanics of how it's going to work. And I.We, we just need to get, we need to get signed up.

**00:16:15 - 00:16:46**
Yeah, I mean, absolutely. So there's the action item. That's the action item. So we need to get sign off. So we have this item. When are we doing that meeting? When are we getting sign off? That's what we need to discuss. And at the end of the day, I mean, if we're, if we can go back and one thing, I'm not putting words in your mouth. I'm just from what I'm hearing and correct me if I'm wrong. We're going to do the live posting. We've mapped out what we believe that means. We need them to sign off on that. Is that correct?

**00:16:49 - 00:16:50**
Say that again, sorry.

**00:16:50 - 00:16:57**
Okay, so what I said was we've agreed that we're going to do the live posting. We've defined the algorithm or how it's going to work.

**00:16:58 - 00:16:59**
We have, yeah.

**00:17:00 - 00:17:02**
And we just need their sign-off before we build it.

**00:17:03 - 00:17:04**
Yeah, that's fair.

**00:17:05 - 00:17:07**
Then I don't know why this is difficult.

**00:17:10 - 00:17:11**
Yeah, so that's...

**00:17:11 - 00:17:11**
You need to do this.

**00:17:12 - 00:17:17**
That falls into some of the outstanding decisions and stuff that we've talked about, unresolved decisions. Yeah, we'll get that.

**00:17:17 - 00:17:56**
But we need to call this one specifically in monday.com and walk through that because it's just things are getting pushed to completion and it's percolating up and it's getting to Sam and Shane. And now they have a long note around this, right? And this is the stressful thing here is this isn't difficult. This is just project management 101. Like, let's document the item. Let's have the conversation with the right people. Who on their side can sign off? It's like, just so we're clear, when we say we present this to ABCRC, who is the person? Not the person with the opinion, not the person who will use it, but who's the person that signs off on our live bat posting algorithm? Who's that person?

**00:17:57 - 00:17:59**
It would have to be Shane.

**00:18:00 - 00:18:45**
Is it Shane? We got a note. So like it was kind of a rhetorical question. This is the stuff you need to look at and think about and say who like David may come back and say, agree with this or Dav may come back and agree with it. But if they're not the decision maker on that item and I don't care who's responsible for it, I want to know who's the accountable person for it. So we need when the response that we come back here with this is it's been it's it's. It's proper, it's now going to be properly documented. Monday. Com with steps and one of those steps. The next step clearly is is to get, uh, alignment on on our live dot, our live posting approach alignment and sign off.

**00:18:45 - 00:18:46**
Yeah, yeah.

**00:18:46 - 00:19:36**
And and when are we doing that? How does it get done? And assuming we do that meeting this week, I don't know if it's available, but if we did it this week, would it still hit release? Four? Right, that's. This is the stuff we need to sweat the details, because when you don't sweat the details, this kind of stuff comes up. It's easy to respond to Sam's note when we have the details, but when everything is vague with, like, he said, she said, this was done, it's really, really hard. And have no doubt, if this hits the fan, it will not be ABCRC's fault, even if it is their fault. Yeah. Yeah, agreed. Okay, so same with four and five, right? So I'm not as concerned about what the answer is. I'm more concerned about are these items captured in monday.com?

**00:19:36 - 00:19:36**
Yes.

**00:19:37 - 00:19:43**
They are. Okay, good. And what is the next step on number four?

**00:19:43 - 00:19:57**
So you can see at the bottom where it says Sam took the action, said, okay, we need to take this away and have an internal discussion. I talked with Dav about this three weeks ago and said we still need a decision on that. So I don't.

**00:19:57 - 00:20:12**
Yeah. So once again, I like I'll say it again. I'm going to say it every time. I don't care about people saying they said this and that. I own the only thing I care about is what is written in Monday dot com. That is our only source of truth. So what is written in Monday dot com?

**00:20:12 - 00:20:14**
It's that we look.

**00:20:14 - 00:20:14**
Yeah.

**00:20:14 - 00:20:17**
Yeah. You want to pull it up right now or do you want to go through the rest of it?

**00:20:17 - 00:21:01**
Yeah. Yeah. Let's look at that right now. I think these are this is I really want to establish this muscle memory. Because right now what worries me is we should be able to, rather than writing that sentence, just say here's the link to this, the monday.com action. The next meeting is on X, and we will get to the job. Anytime Sam says we'll take it away and have an internal discussion, Sam, okay, what's the date you're going to get back to me, and I'll put that in monday.com. And so either Sam. I still have more time, and our answer back to him is, Sam, it's with you, and you have until X date to respond, or no, you're late, and we were going to chase you down.

**00:21:02 - 00:21:03**
He's definitely late.

**00:21:04 - 00:21:07**
I don't know. Is he? If there's no date, he's not late.

**00:21:08 - 00:21:10**
They've been sitting on it since February 4th.

**00:21:10 - 00:21:12**
If there's no date, he's not late.

**00:21:15 - 00:21:17**
It's taken a while to open. Yeah.

**00:21:19 - 00:21:31**
Like, I apologize if this is coming across a little firm, but I've been having this conversation for 18, 24 months, like across four different product managers here. Monday.com is the only source of truth. Everything else is irrelevant.

**00:21:39 - 00:21:43**
Sorry, do you want to see the risk register or the action register, Roger?

**00:21:43 - 00:21:50**
I just want to see this, whatever you use to track these items. Like items that need to be closed.

**00:21:50 - 00:21:52**
It's both Actually.

**00:21:52 - 00:21:57**
You don't think yeah, I don't know the difference can't see my screen right now No.

**00:22:22 - 00:22:26**
Nothing yet. It's coming up.

**00:22:42 - 00:22:44**
Yeah, I can see it.

**00:22:59 - 00:23:00**
Does it come up yet?

**00:23:01 - 00:23:08**
Yeah, it's up. I'm just looking. ABC, there's the open action items, and it looks from 5 all the way to 48.

**00:23:09 - 00:23:15**
Yeah, there's quite a few, actually. It goes down to 95. Bunch are closed. I'm just looking specifically.

**00:23:22 - 00:23:30**
The obvious really, really concerning thing here is the target close date. Like most of these items don't have a closed date.

**00:23:30 - 00:23:40**
Yeah. So this is relatively new. Keep in mind. Right. So nothing like this existed until a couple of weeks ago. I had to go back through seven, eight months of transcripts.

**00:23:40 - 00:23:50**
But as you create the item, a date should be assigned. Right. Like how do you how do you know dependencies? Anyway, that's that's a broader conversation. But what I want to get to is.

**00:23:50 - 00:24:19**
Your point is valid. This is something that is now part of DAB and my regular cadence at our PM meeting is to fill this, like complete filling this out. So he signed off on it last week because I sent him all of the information saying you need to look at all the action items. If something's missing or something's not right, let me know. We'll work together on it. And then we make it part of our regular cadence to go through all the action items and risks at each meeting going forward.

**00:24:21 - 00:24:35**
Yeah, I mean, I'll leave it to you guys how you want to manage your reviews. Obviously, the ones that I'm hoping you're reviewing first are the ones that are largest impact and coming up soon. But we don't know which ones are, like where the dependencies are, right?

**00:24:35 - 00:24:42**
Yeah, so you'll see like number 42, confirm whether diverse is must or now QC extrapolation, right?

**00:24:42 - 00:24:44**
That's an action item. Is that item four?

**00:24:45 - 00:24:47**
A42, A042.

**00:24:48 - 00:24:55**
Yeah, is that the item that? Shane, sorry, Sam picked out Resolve Now Financial Data Retrieval Gaps.

**00:24:56 - 00:25:11**
Yeah, you'll see that he's talking about the extrapolation outputs. That's the action item. And it's assigned to DAV right now. They have to confirm whether...

**00:25:11 - 00:25:17**
So just so I'm clear, 42 is item four on Shane's list, is on Sam's list.

**00:25:18 - 00:25:19**
I don't have it open, but yeah, probably.

**00:25:20 - 00:25:28**
Okay, so assuming that's the case, then our answer is going to be back to him. It's tracked to number 42, and it certainly currently sits with ABCRC.

**00:25:28 - 00:25:29**
Yep.

**00:25:29 - 00:26:13**
And so who's the owner of it? It's DAV, right, David? DAV, yeah. Yeah, and it has no closed date at this time. And what is the note? So that's the answer to Shane. I was just saying, I don't want to get into he said, she said, coulda, woulda, shoulda. It's per the source of truth, A0042. It's been open since January 21st. It sits with DAV right now. That's the only response you need to do. I don't know if there are subtasks associated to getting this item closed.

**00:26:16 - 00:26:16**
Not presently, no.

**00:26:18 - 00:26:21**
So what are you waiting for, Dav? What are you waiting for?

**00:26:22 - 00:26:58**
So they have to provide an answer, whether the diverses must store the NAVQC extrapolation outputs, because that was the meeting that we had with David and them, and David said, we're paying you guys money, you have to do this, and we pushed back saying, but why do we have to do this? Like, it's a bolt onto our product, it doesn't fall within the SAS framework, et cetera, et cetera. And that was where Sam said, OK, we need to take this away and have an internal discussion about it. And there was no feedback since then. So that's what I called out a couple of weeks ago, saying we still need to understand what your position is on this.

**00:27:01 - 00:27:11**
OK, yeah, I'm sorry. I'm just trying to parse the language there. Mark, you're on the same page. This is the same issue.

**00:27:21 - 00:27:22**
Yeah.

**00:27:22 - 00:27:23**
Okay. Extrapolation, yeah.

**00:27:24 - 00:27:47**
Okay. So the answer back to them is we're waiting for some answers. Confirm whether to store NAV QC extrapolation output or only surface them in NAV. Okay. So that's our answer back to them. All right. Good. Resolve post-extrapolation data flow number five. Define how volume and dollar values will flow from NAV to diversus after extrapolation.

**00:27:47 - 00:27:49**
The same thing. Same issue.

**00:27:50 - 00:27:52**
So it's also 80042?

**00:27:53 - 00:27:53**
Yeah.

**00:27:56 - 00:28:15**
Okay. All right. And then 678, sorry, not 8, 67, those are also in the open action registers? I'm not sure.

**00:28:15 - 00:28:17**
I'll have to, it's 167 document.

**00:28:19 - 00:28:20**
Talking about quality control scope.

**00:28:21 - 00:28:43**
Yeah, so that's part of it. What they need to do is, like, we presented the quality control scope. We've even presented and showed them what random, random, target random, and target QC looks like. It was demoed to them. It's in the product right now. And DAV has a takeaway to go look at that and make sure or validate that it meets their requirements.

**00:28:44 - 00:28:54**
So Dab's takeaway, can you show me in monday.com where that is? That action, Dab's takeaway? I want to make sure Dab's got his takeaway.

**00:28:56 - 00:28:57**
Yeah, it's in here somewhere.

**00:29:19 - 00:29:20**
I know it's in here somewhere.

**00:29:21 - 00:29:49**
Okay, so you don't have to find it. So if you're confident it is in here, I will trust you on that. That's fine. So my ask is, what is your target date to get all of these dates closed? Like you have target close date for each and every one of these. Do you have a target date with them? Because if you do bits and pieces, I mean, the project will be done by the time we get it done, right? And there may be some urgent. Pieces in here.

**00:29:49 - 00:29:59**
There's, there's in his document and share NAVQC challenge rules.

**00:29:59 - 00:30:10**
So it's been open since December 2nd. So I can see where Jane is, or Sam is, is is raising this. So when are we like for the target close dates? When can we have all those dates done?

**00:30:11 - 00:30:32**
That's what I need to talk to DAV about. So, again, going back, like a couple weeks ago, none of this action register existed. I had to go back and build it all from scratch. So now it's there. So now we're aligning everything. So I first made sure that DAV was in agreement that these are the outstanding actions. Now we need to go through it week by week and say, okay, when are they closing?

**00:30:33 - 00:30:41**
Yeah. So can we get all of these closed by the end of the week? Not closed, I mean target dates. We need dates on these things.

**00:30:41 - 00:31:01**
Yeah, that's our discussion tomorrow. So last week we had Mark join the call, so we postponed doing this work for that. He had some questions around the product and stuff. So we've agreed that this week this is our focus, is to go through all of the action items, target dates, the risks, et cetera.

**00:31:02 - 00:31:05**
How many items are there?

**00:31:06 - 00:31:09**
Oh, there's probably like 50 that we need to go through here.

**00:31:10 - 00:32:04**
At the bottom, it doesn't say a total or something. No, no, no total. It's for these. These are all the outstanding items. OK. Yeah. And these are all. So this is what I wanted. So we've closed quite a few as well. Yeah. Yeah, it's good. I mean, it's great. You guys are closing and I think this is good progress. But the muscle memory I want to instill here is. This is our only source of truth. If it's not here, it's not part of the project. This gives us a defensible response back to all of Shane's questions. And we can say, look, it sits with whomever, any of these items, and we're closing in on target close and dates, and we will have the target close dates by, I mean, I guess the question would also be for Mark, which of these items he needs closed?

**00:32:05 - 00:32:30**
In order to be able to finish the specifications to deliver. So it's not just a numerical, we're going down the list. Mark should be a part of these conversations with DAV to be able to say, okay, there are X number of items here. These are the ones I need closed first so that Mohsen can write the specs. That needs to happen. So what do you think, Mark?

**00:32:32 - 00:33:33**
Yeah, I mean, It has been a little bit of a while since we sat and reviewed all outstanding actions and items, at least my involvement in that. So I think it would be a good exercise just to go through it and just make sure we're all on the same page. And like you said, prioritize those that have the biggest impact on what we're doing right now. And have the biggest risk to the timeline and the dates. We've kind of bundled a lot of it up into API integration. That's kind of been the one thing we constantly talk about is API integration. And it's on pause. You know, it's not. We can't agree. So, you know, I know it's broken out more, so we can go into each individual component. I don't think there's that many, to be honest, related to the product.

**00:33:34 - 00:33:44**
Okay, so if we could go through those and then you get those, because I just want to make sure that Duane and Dav don't give a date to a certain thing and you're like, well, I need that three weeks earlier.

**00:33:44 - 00:33:50**
Yeah, yeah, yeah. For sure. Yeah, we could do an exercise and take very long.

**00:33:50 - 00:34:08**
Yeah, I mean, I think that's the priority. I think things need to be bucketized into priority one, two, and three, right? Priority one is what does the product team need? Yesterday, two is what are they going to need tomorrow? And three, what can wait a little bit longer. I mean, the reality is we need.

**00:34:08 - 00:34:11**
Reality is we need everything now. Like, Yeah.

**00:34:11 - 00:34:33**
I mean, that makes this even more urgent, this activity even more urgent. Like that's where I'm worried. That like, if we can't wait for for like we. We can't have dates on this stuff at the end of April, because you may come back. I needed this weeks ago, so we, we need this. These date close dates aligned with ABCRC, um, we need those dates to find, I would say by the end of this week.

**00:34:33 - 00:34:42**
Yeah, for sure, for sure. Like, if they want to, yeah, if they don't want to phase, I mean, phase four is no.

**00:34:42 - 00:35:17**
I I think the first thing is, when do we get to an answer of an answer? So let's build that so then at least we can have a conversation with them on these points. But if you've got, maybe it looked like maybe 45, 40 to 45 items, if each item take, maybe. You need to book four hours out, right? You tend, I don't know how long, or do it over three days, but I think it needs to get done. And so when we so, the benefit for that then is for all of these feature action items. You just reference the Monday. Com.

**00:35:22 - 00:35:29**
I think the only one that's not in there, Roger, is the live versus batch. I think that's the only one that I haven't captured on the list.

**00:35:30 - 00:36:01**
Okay, so we need to put that in there. Yeah, I need to put it in. And when is it going to get closed? I mean, I get that David wants to do something, and we haven't even had a conversation around what his motives are, but if we were just to say we put that item in here. When does a decision need to be made from a technology perspective? Maybe not. I mean, if we're already putting into phase four. So you just need to track down there. How do we get there? And it sounds like it's with that.

**00:36:01 - 00:36:05**
I think the risk is that what we build doesn't meet the need.

**00:36:06 - 00:36:48**
Yes, we have to get signed. You're right. That's the action, right? So there needs to be an action, a subtopic in there that basically says diverseness provides the spec. Or the algorithm or whatever you're providing to them by date X, and then our comment will be back to them. Who, who reviews that document? We need to know, so that's the question would be, who does it go to and don't? So we don't just put it goes to ABCRC? That's not used. That's not productive. It needs to go to so and so, and then the action is assigned to that so and so person. They will provide feedback within whatever you agree on as a timeline one day, seven days, 14. Whatever it is, shouldn't take very long.

**00:36:48 - 00:37:12**
And then if they sign off on it, it's closed, if they don't sign off on it. There's a discussion period of a couple days with an action, next step, actions. That's. That's the kind of clarity we need on this and this. That will negate all these concerns. Because I really don't want to send Shane comments around, like he said. She said. I want them to be able to reference Monday.com as much as possible.

**00:37:13 - 00:37:17**
Do you remember, Mark, when that document was sent to them, the live batch?

**00:37:21 - 00:37:38**
The date on the presentation was January 20th. January 20th. So it's around that time frame.

**00:37:39 - 00:37:50**
They're closing on three months. Yes, it's their bad for not providing feedback in that period, but it's our bad for not tracking this and following up.

**00:37:52 - 00:37:52**
Yeah.

**00:37:54 - 00:38:02**
Everything just needs to be in monday.com, and we've got to get away from, do you remember when this happened or any of that? That should all be captured in monday.com.

**00:38:02 - 00:38:07**
Yeah, that's where we've moved to, but there's still some things to do there.

**00:38:08 - 00:38:09**
Okay.

**00:38:09 - 00:38:09**
Yeah.

**00:38:12 - 00:38:14**
And then the other items. Those are the same.

**00:38:15 - 00:38:30**
The driver thing is, I mean, we included what was in the release. It wasn't client-specific. So, I mean, that's the answer. Slide four is not client-specific. The driver app is represented as part of the release. It's not applicable to that. So it's just noise.

**00:38:33 - 00:38:40**
It was standing business. The driver app belongs to Encore Pacific. Yeah, it doesn't belong to anybody. It's just a feature. In our software.

**00:38:40 - 00:38:44**
Yeah, that's the response. It's not client-specific. That one's just noise.

**00:38:44 - 00:39:02**
Number nine, identify any business decisions of an API as if any exist. That should all be in monday.com. Dude, open up Monday. Sit with your project manager, DAV, and all of the actions that are due are in monday.com. And we have to be confident that's a correct statement, but it has to be true.

**00:39:02 - 00:39:12**
And that gets back to the comment in number one, right? Delayed feedback. So he's asking about, is there other phases beyond phase four?

**00:39:13 - 00:39:42**
No, I read it as, are there other business decisions that need to be made? I don't want to get into, like even number, yeah, everything just needs to Monday.com and get everybody into that muscle. So it should be all outstanding decisions reside in Monday.com. And if we can walk through those. And do you guys have? Regular time you have, you and Dav have walkthroughs of all the actions, right?

**00:39:42 - 00:40:06**
Yeah, well, starting tomorrow, yes, because all of those action registers and decision registers, they didn't exist until a couple weeks ago. So, and and they weren't in Monday.com, none of this stuff was tracked in Monday.com at all. So I had to go back through like eight months of transcripts and meetings and stuff. And pull all of that information out to create this stuff to get us to this point. Yeah, yeah.

**00:40:06 - 00:40:18**
It's bonkers. And then 10, identify unresolved field definitions or documentation gaps blocking downstream activities. Do you know what that means?

**00:40:22 - 00:40:53**
Yeah, that's related to the document, the API document. So when we met with Dav last week, he was trying to do mapping from what they require in NAV to what the API spec was, but he finds the API spec. Unclear, doesn't have a mapping table that he wants. So Mark had indicated that he had spoken with the development team and they're going to update or enhance the API spec document to make it clearer on the mapping stuff.

**00:40:54 - 00:41:01**
And that's in monday.com? Is there a date in monday.com for that task? No. Or is that task even in monday.com?

**00:41:01 - 00:41:03**
Not yet. No, that's a brand new task as of Wednesday.

**00:41:04 - 00:42:02**
Yeah, as soon as it's created, we just put it in, just like on the spot, just like muscle memory. A new task, it goes in. Because otherwise, if we don't know monday.com, I mean, it could be nearly a week late, right? Yep. If it was last Wednesday, that's a week ago. So just put it in on the spot. And so then with the item here, we can go to Sam and say, here it is, item 00 whatever. We're updating that documentation document. And a subtask should get signed off on by them. And signed off doesn't mean they're going to change it. It just means, yes, this meets their needs. 11, revise project status messaging to explicitly reflect ABC-raised concerns. So we can discuss that for the next project, the end-of-month review. Reasons, reassess overall project status.

**00:42:04 - 00:42:53**
I don't know what he wants to reassess. I don't understand what that means, but we're going to keep, we're just going to keep submitting what the project, if it's defensible, we are going to present this unless he can come back and explicitly say, Sam, what would, which one would you change? Which, which stoplight would you change and what color would you make it? And please explain why. What his concern is, he doesn't want his deliverables to be red, which is fine, which is exactly what I, like before Mark joined, I said, I was actually very happy with Sam's note. Because it shows he's realizing that his team is, they're falling behind and they don't want to be seen as that. Yeah. Clear actual resolutions before APA. Yes. Monday.com. Everything that we're doing with task owner due date is now in monday.com.

**00:42:54 - 00:43:45**
And prepare to review all in the next meeting with Dave. Good. There's going to be a meeting at the end of this month for sure. They're going to want it, which is awesome. Yeah. But to do that, Monday.com needs to be very tight every day. None of this, it was last week. It needs to be in real time. Yeah. Is there even ways to extract from emails and other things and load it into Monday.com? Yeah. It's just a time where like Copilot or Claude or something extracts it and puts it in. I don't. I know monday.com does have some capabilities, but stuff we need to look at. So my main takeaway here is get away from he said, she said, and when things happened, accept that monday.com is the only source of truth we're going to talk about.

**00:43:45 - 00:44:28**
When we get on these meetings at the end of the month with them, the only source of truth is going to be the ABCRC action register. The week before. The meeting, we have to send them a note and say, please review ABCRC action register in monday.com is that will be the only, that will be the source of truth. Everything else is irrelevant. And we got to get into that habit. They like the habit of being able not to, because when it's unclear and it pulls, it makes us unclear. They win. They win those arguments. We're not going to win an argument where it's in an email or he said, she said, it's you fight that you're going to lose. The only way we can win is monday.com. You've got to get better at it.

**00:44:29 - 00:44:47**
Yeah, we've landed on that between Dav and I as well, that that is the source of truth. So I went through all of this effort to put it in there, and I told Dav that that's the source of truth now. That's what we're going to be reviewing as part of our cadence every Wednesday. We're going through the action items and doing updates and so on.

**00:44:49 - 00:44:50**
It sounds like it's still missing a few items, right?

**00:44:51 - 00:44:58**
It is because it's new. I didn't walk into this eight months ago when this was done. I had to produce this.

**00:44:59 - 00:45:09**
I'm talking in the next few days. I don't really care when it was built. What I'm trying to say is it's still 90% there, but it needs to be 100% or at least 99%.

**00:45:09 - 00:45:12**
Our first goal out of it is tomorrow.

**00:45:13 - 00:46:07**
And the dates. You need to sit with Dav and say, look, Dav, we need to be able to properly respond to these. We need these dates. So we have to respond to Sam today. I think our overarching message is going to be a lot of these items are being tracked in monday.com. And we're going to use that as the basis for going forward. And so the items you raise for many of the specific actions you're raising are in monday.com. I'm working with DAV on those right now. You can always access monday.com. We will have a deeper review at the end of the month. Do we have a scheduled meeting with them? Nothing yet. You have to work with DAV to put something into the calendar. I would imagine it's going to need to be an hour at least.

**00:46:07 - 00:46:49**
That was the request. Maybe an hour. No, it shouldn't be too long. The reality is these meetings with the execs shouldn't be too long because they should already be aligned what it is. They may have a question or two, but if we have to walk them through what an API is, that's a separate session, right? So my ask would be, yeah, if you could dig up that image that you did for the API, I think we need to prepare that. Because your message to DAV needs to be you're not clear on what an API is. Here's once again another visualization. And maybe we'll add that into the review deck and say all of the endpoints are done. They've been done for forever and a half. We're updating the specification document.

**00:46:49 - 00:47:24**
That will come out whenever engineering is releasing it, and you need to get a date for that. All your other points are tracked in here. It's 00042, 000 whatever. You have that stuff. You're tight for that meeting. You don't, and it becomes a he, she, said. Do you remember in the January meeting? You're dead. Yep. It has to be monday.com, and I'm going to keep harping on that constantly. Yeah. All right. Anything else?

**00:47:25 - 00:47:39**
No, I think that's it. So, Mark, if you could send me that presentation that was – sent to them on the 20th. And if you can provide an update on when you think Dev will have the API spec document updated, that would be helpful.

**00:47:40 - 00:48:30**
Yeah, the spec came out Friday from engineering. I need to review it. I looked at it over the weekend, but there's some things that I want to make sure we describe clearly to them. So yeah, it'll come out. Either today or tomorrow for it, for them. Um, yeah, on the deck, I want to, I was just looking at the deck again. And I just want to make sure it reflects the latest conversation on the events because the events are part of the deck. So, you know, the agreed events that we said we would support just need to be accurate. If we're going to resend it to them. Okay, yeah. I just want to review it. That's the big sticky point is those events. And if we send out an updated version and it's not accurate then.

**00:48:33 - 00:49:18**
So I think our note back to Sam at this point today, it needs to be very, very simple. It just needs to be all of your action items that you're referring to right now are tracked in monday.com and I review them with DAV. We will review with you and the broader team at the end of the month, and I will work with DAV to schedule a date. Yeah, I think that those are the only two sort of real points. If you want something intermediate, happy to jump on a call and get into it. We're not going to reassess overall project status or anything messaging for the April deck, but the end of April deck or May or whatever. I mean, it is.

**00:49:19 - 00:49:34**
I don't think we would reassess it any differently, to be honest. I don't think any of the soft lights are going to change. The colors are what they are. I had Dab review it as well, and he agreed. That's a fair assessment.

**00:49:34 - 00:50:13**
Yeah, you can't throw Dab under the bus. You definitely don't want to say Dab reviewed this and he signed off, because that's going to... No, I didn't. Yeah. But... Without dates on the open action items, how do we even know we're good? That's what I would ask if I were Sam. Like if I went into Monday.com and there's 50 open items and 90% of them don't have due dates, how can you possibly say diverses will be done on time when we don't have dates? Because you guys need sign-off from us to close. You don't have sign-off from us. You don't even have a date to get a sign-off. So how can you be green? I think ultimately what he's looking at, he doesn't like that we're green and they're red.

**00:50:15 - 00:51:12**
Yeah, that's what he is, that's what's annoying him, because if he knows that we're positioning, at least he should know. Um, yeah, that's the way we get into that. You have to have data to support it, data-driven decisions. We came to green because these items, but the reality is, maybe he's got a point, right? Like we say, all these things are green. I.We have certain features that we're delivering, but it sounds like we don't have their sign off on it. So from their perspective, It may not be features they can use, which to them is not green. So. Yeah. OK, so let's let's so we have to sort of phrase a very short email to Sam just to recognize that because you can't just we just can't not respond. And in parallel, we got to just.

**00:51:12 - 00:52:23**
Iron out Monday. Com. Between now and the end of, and between now and the ABCRC meeting, hammer it out. And which means it needs to have clear owners and and so one thing, I, yeah, you actually do have the owners there, you have DS and stuff, so that's good. Um, yeah, so for my own sanity, um, when our next? So our next touch point is that? When is our next touch point? I don't see anything in the calendar on this. I think almost we should be doing something, even if it's a 30-minute touchpoint weekly. Yeah, we need to get this back into the calendars. I mean, I would, I think. Duane, for you to be able to do this effectively on dates and stuff, you definitely need Mark's input on a lot of these items. Yep. So you need to go through those 50-plus open items. Are there anything missing?

**00:52:24 - 00:52:31**
Yeah, the priorities from a dev perspective, product and dev perspective, sure.

**00:52:32 - 00:53:05**
Yeah, I mean, whatever the action. I mean, some of these items are not necessarily Dev per se or so, or they may have be Dev. I don't know, I haven't gone through all 50 but and and please consider, are you missing anything? Yeah, anything that requires something to happen needs to be in in in that document. Yeah, in the Online.com. It can't be tracked outside, or when we email sent, it should all be documented, like, how do like? If Mark were to send that document, does that get tracked in Monday.com? How do you know a task has been completed, that type of thing?

**00:53:05 - 00:53:16**
The idea is that for each action that's in there, if documents are provided, that's the source of truth. So we attach the document to that action item. So we can always refer back to it.

**00:53:17 - 00:53:20**
Okay. And you'll be able to reference, I mean, yeah.

**00:53:22 - 00:53:34**
That's the idea. And any comments and stuff that are, you know, like they get. Logged there, not in an email and so on. So that that's the. The whole go forward is is to have everything that is the source of truth for everything.

**00:53:34 - 00:54:12**
Okay, yeah, I do want to have a another touch point next week, and I'm. I'd like to see most of those action items, if not all of them, closed, like, at least with dates. Yeah, I mean, you can dates can get revised, but I want to make sure it's got dates and I want to make sure Mark has seen those dates and he's like, yeah, that those dates work for me to be able to deliver. Yeah, that's fair. OK. OK, so. Yeah, so I'll let you book the next the next touch point. Yeah, we'll go from there. Okay.

**00:54:12 - 00:54:29**
Yeah, and as far as the meeting goes with ABCRC is, yeah, we've offered it to them. I've talked to DAB several times now about starting that monthly exec meeting back up, and they've been pushing back, saying no. So hopefully this changes that.

**00:54:31 - 00:55:20**
Yeah, yeah. I mean, as long as we have veryclearmonday.com and we've sent those monthly status updates, the meeting is for their benefit. But we need to have those two things. We have to have the monthly status basis and we need to make sure that he's clearly going to say if we have it under red still, he's going to want to understand how we got to those points. And the only source of truth is going to be monday.com. I know I sound like a broken record, but it's all going to feed back to that. On a separate, completely separate note, Yeah, we have – Mark, today you have the AI demo, I think, right, which will be good. Any questions on that?

**00:55:22 - 00:55:22**
No.

**00:55:22 - 00:55:23**
I think it's pretty straightforward.

**00:55:24 - 00:55:24**
Yeah.

**00:55:24 - 00:55:25**
Good.

**00:55:25 - 00:55:32**
Well, I guess the three of us will see that. I'm actually going to be driving at that time probably, so I may not have the camera on, but I'll be in the car.

**00:55:33 - 00:55:33**
Okay.

**00:55:34 - 00:55:39**
Even for – I noticed we have a 3 o'clock meeting. If we want to do that today, then that will probably also be in the car, if you're okay with that.

**00:55:41 - 00:55:45**
That's about the roadmap. Yeah, that's okay, sure. If you're okay doing it from the car. Yeah, yeah.

**00:55:45 - 00:55:48**
Yeah, okay. If you're okay with that, then that's good.

**00:55:48 - 00:55:50**
I can push it later if you prefer.

**00:55:50 - 00:56:01**
No, no, that's fine, as long as you're. It's nothing really to show. Um, no, yeah, okay, perfect. Okay guys, thanks so much, all right.
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="c4be8793baca1e7f">>>
</file>
assistant: I don’t have this one in the ABCRC client transcripts folder yet, so I’d process it as new.

If you want, send the next one and I’ll keep going.
user: Did you process the last one?
assistant: Yes, I’ve processed it now.

Created:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-07 Internal ABCRC Project Management and Communication Alignment.md`

Send the next one.
user: [media attached: /home/duane/.openclaw/media/inbound/2026-04-01_Dav_Duane_Data_Mapping_and_API_Integration_Challe---214392b7-38dc-47ea-ac69-9be7d1a84b28.md (text/markdown) | /home/duane/.openclaw/media/inbound/2026-04-01_Dav_Duane_Data_Mapping_and_API_Integration_Challe---214392b7-38dc-47ea-ac69-9be7d1a84b28.md]
[Discord #alfred-main channel id:1478436599074258954 +13s Thu 2026-05-07 13:37 UTC] Leitchy (dl_70): <media:document> (1 file)

<file name="2026-04-01_Dav_Duane_Data_Mapping_and_API_Integration_Challe---214392b7-38dc-47ea-ac69-9be7d1a84b28.md" mime="text/markdown">

<<<EXTERNAL_UNTRUSTED_CONTENT id="cc7b952147755acf">>>
Source: External
---
# 2026-04-01 Dav:Duane Data Mapping and API Integration Challenges for R Bill and NAV
Creation Time: 2026/04/01 11:29


## Transcription

**00:00:17 - 00:00:18**
Good morning.

**00:00:19 - 00:00:19**
How are you doing?

**00:00:21 - 00:00:22**
Doing okay.

**00:00:22 - 00:00:23**
Just okay?

**00:00:25 - 00:00:26**
Yeah.

**00:00:26 - 00:00:27**
Yeah? What's up today?

**00:00:33 - 00:01:46**
We're struggling on our end, to be honest with you, Duane. So in one of the emails I was sharing with you about the data, so unless David and I are completely wrong, I just picked up one of the transactions that was claimed ready, which means that it's got to be sent to NAV for payment, right? And so we were able to map some of these. UH, Fields Oh, let's move that over here. So it's easier to get to the information that's in the API. Okay, but what we couldn't do is match up this stuff. Is this stuff going to be transmitted as part of the our bill? Yeah, that's what we're trying to figure out, and this is not in. Right, so we would be expecting, in simplest terms, everything on this page, right, which is the R bill, would be transmitted to NAV.

**00:01:46 - 00:02:47**
So it would go to the endpoint, NAV would pick it up and import it, right? So this is the R bill, right? And the R bill needs to be transmitted. We have a number here, and then we have the word units. Okay? So I don't know if this is two fields. I don't know if it's a single field. If it's a single field, then obviously it's going to be alphanumeric, right? But if it's two separate fields, well, then this one would be alpha, and this one, sorry, numeric, and then this one alpha. But because this has a comma, is this going to be an alphanumeric field? So that was what was in the email that we were trying to understand, like this data structure, because here we go. This I have category up.

**00:02:48 - 00:03:20**
So field size is 50 characters, 200 characters for description. It's a Boolean in this particular thing. And list of options. Okay, so we have it for the category. But since we're talking about product, then this is what I was trying to map to. Because that's how I interpreted this. Right? Because this is product here, it says product here, so if this is a product, right.

**00:03:20 - 00:03:38**
That could be coming from shipping package though, right? Sorry. I say it could be coming from the shipping package API part. As opposed to product, you know, you know what I mean?

**00:03:40 - 00:04:55**
Right. I was just using that as an example because. Yeah. So here's site, right? Here's shipping containers. But shipping containers, this is the API. It's not the data, right? So if this is the R bill, we should be able to map the data to each of these. And that's where we started struggling. So like I said, like the site information, which is this top information, right? It's mappable because we got it here, right? It doesn't really address it. Like it says business name. 60 is the field size, right? But it doesn't tell us if it's alphanumeric or just alpha or numeric or open text field. This one has it, okay? That tells us we can include these special characters, which is great. So some of them have it, okay?

**00:04:57 - 00:05:19**
But again, that's... the site information, but it's the stuff down here that's the critical stuff, which is the R bill. How do we map it to these things that are in the API document? And so that's what I was asking in the email yesterday.

**00:05:19 - 00:05:20**
Right.

**00:05:21 - 00:06:07**
How do we map it so that we know what type of fields these are? And so that's what David's saying. He doesn't understand the flow of the R bill that once it's claim ready, remember, once it's claim ready, it means that it's to be sent to NAV for payment in NAV, right? Right. Yep. Okay. So all the other stuff that happens in here, adjustments and all that, yeah, that's there. But once it's claim ready and gets... sent over to NAV, we have to be able to map the corresponding fields. So that's where the question is coming from.

**00:06:07 - 00:06:17**
So in NAV, does David require every single one of these fields to be mapped into NAV?

**00:06:18 - 00:06:20**
Yeah, we have to map it into NAV, yeah.

**00:06:20 - 00:06:42**
No, I'm just wondering, because there might be some stuff that's on the screen that David doesn't require. So I don't know which ones he may not require, but I guess that's the question, is does he, like everything that's in those columns, consider them columns, is everything in those columns required to be mapped into a field in NAV?

**00:06:43 - 00:07:25**
Yes. So that's what we were working on yesterday. So everything in this R bill has to be mapped into NAV. So everything except. Transaction history Right the lap, it doesn't need all of the transaction history. It just. And that was something else I I couldn't figure out. Um, and I'll go through that in a minute. Um, there's only one line in here that he would need. Okay, so this is a claims ready transaction, which means it's ready to go over to NAV. Okay, you see, it says here received to claim ready.

**00:07:28 - 00:07:29**
Okay?

**00:07:29 - 00:07:47**
There's no other line here. How do I explain this? That tells me, because for the first little while, we don't know when you guys will have it in real time, it's going to be a batch file, right?

**00:07:49 - 00:07:50**
That's my understanding, right, yeah.

**00:07:51 - 00:08:59**
Yeah, so let's just go with the batch file for now. Okay, so if it's claimed ready, this would be the time stamp that would need to be sent over. So who made it at the date time, who made a claim ready? And I guess the it should be a line like status is claimed ready, or, uh, status is, um, sent to NAV or something like. That's the only line he would need as part of the R Bill. Okay, because currently right now, when they are now and they click Claims ready. There's fields in the database that actually has this information. That make payment is this date, time, who, who's authorizing the payment, and then there's a status of we'll use the word claim ready, okay. So I asked David, could he accept this transaction status change from received to claim ready?

**00:09:02 - 00:09:14**
We'd have to do programming changes in the database for that many characters because basically the field just accepts the word payment ready or in this case claims ready.

**00:09:18 - 00:09:38**
That might be something that when the information is being sent over, so your API connection, that the API connection could just truncate that and remove anything that's prior to claim ready and just send David what he needs. So he wouldn't need to make changes in the database necessarily. It would be part of the connector, just strips out.

**00:09:39 - 00:10:01**
Okay. So let me ask you this question. Let's go that that's a possible solution, right? Okay. What size is this field? So that the developers can truncate in the API, please ignore, I don't know how many characters are here. We'll just say, please ignore the first hundred characters and just accept claim ready.

**00:10:01 - 00:10:50**
Yeah, they would just do it through coding. So it basically wouldn't matter how many characters are before the C or the word claim. Programmatically, it would just say anything that's before claim, get rid of it. So it could be five characters. It could be 55 characters. The program doesn't care. It just looks for a claim and says strip everything before that. Excel works the exact same way. You can just do a quick function in Excel to say, like, look for this word and delete everything that's before or after it. Yeah, that they wouldn't have a problem doing. I mean, they've probably done that a million times. But it would just be to make sure that whatever David needs, that's only what's being sent over in that connector. So I don't think that's a big problem.

**00:10:51 - 00:11:35**
But I like what you guys have been doing and going through and mapping this stuff because that's the information that the product team needs. It's like if you say, I don't know, let's say there's 20 columns here and you can only clearly see mapping for 17 of them. So there's three fields that don't seem to map clearly. To Nav. And either they're they're not there currently in the API and need to be there, or they are there. We just haven't found the right spot yet. And so that that's the conversations we need to have with Mark and team, and that's the feedback that we're kind of looking for is because if they are missing and David needs them and they need to be put into the API, then that's what Mark and them need to know. So they can plan it and get Dev working on it.

**00:11:36 - 00:12:41**
Right. And so sort of that's what I was providing the feedback yesterday going, I can't map this section, right? This section here was what I couldn't map. And so I was saying, what am I missing here? Because I was using the API documentation, right? So I'm just going to make this up. Maybe estimate quality of product is actually called category, right? So I don't know. I couldn't map this collected section, all this detail to the API. So I know what type of field it is, what type of, what it is. So that's what I could not do. Okay. And then David and I had a working session with our nav mapping. And yeah, I ran into the same problem, you know. We were able to do this right because it's very clear, but we weren't ready, we couldn't do this section and then this is what came up.

**00:12:41 - 00:13:01**
Because he doesn't need this type of history, because that's not important. Because he's just going to take the our bill that is ready for payment and that's what he's, that's the line he's looking for, right? Okay, and so that was. The other thing is, I couldn't map this.

**00:13:03 - 00:13:45**
Yeah, I did a quick, just a quick table lookup yesterday. So it was quick and dirty. Just because it looks to me like a lot of this stuff, like the shipper, for example, that's in your, like if you go to the transaction where it says shipper, that comes from the participant API piece. If you look at status, that comes from the transaction API V1 slash V2. The receiver comes from the participant section of the API. The site obviously comes from the site. API, product comes from the Recovery Stream API category, Recovery Stream API.

**00:13:45 - 00:13:51**
Uh, go back, sorry, sorry, go back to product that goes to what?

**00:13:51 - 00:13:57**
So the product says it goes to the recovery stream API.

**00:13:57 - 00:14:00**
Okay, so let's.

**00:14:00 - 00:14:32**
So the end-of-life products section. And by the way, I just did this quick and dirty dive, so I may not have it 100% correct, but the point was that all of these things map to different sections, right? So where you're looking for stuff and you're thinking, oh, you know, the product I think should be in this section, but it might actually be in a slightly different section. And I can share this with you as well, just as a reference. Under the acknowledgement that it might not be 100 correct.

**00:14:32 - 00:14:37**
Oh yeah, yeah, yeah, anything that can help me. Yeah, I'm just trying to.

**00:14:37 - 00:15:03**
I'm just trying to help. Because, because, like, when I, when I, and. And of course, I think we need to involve Mark and them for the deeper dive on that. But it shows, uh, the vehicle even shows to me, at least when I looked at it quick, it said. Transaction History Slash, Advanced Flow API section. Time stamp, transaction history, audit trail, of course, transaction history.

**00:15:04 - 00:15:18**
But let's just go back, okay? So I'm looking at end-of-life products, right? Yeah. Okay. So this is the API development.

**00:15:19 - 00:16:10**
Yeah, so in the quick and dirty I did, it said, It says likely API field concept for that is, so the product says recovery stream API, end-of-life products is where that seemed to fall. So likely API is the product, of course. Makes sense. Okay. Because it says in the quick notes that I got, and by the way, I used some AI to help with this, because I wanted to have something ready for you today just to sort of help. But it says the API docs define product data structures separately. So it may not be under product, but it looks like it's under end-of-life product or in the recovery stream API.

**00:16:12 - 00:17:01**
Okay, so I'm just looking at the end-of-life. This is page 58, okay. If I go back to the beginning here. Nope, wrong way. So these are the endpoint definitions, right? So we have the shipping container, we have the category, we have the product. Okay, I'm a participant. All right, so I'm just looking at product. So now I want to go back to 55.

**00:17:03 - 00:17:13**
Yeah, so in there you'll see where it defines name and code and all of that. So product comes from there.

**00:17:14 - 00:18:29**
Code product code comes from there right okay yeah we saw this right okay so now we'll go to page 55. Okay, here we go. Oh, that's the token, sorry. It's a page. Short direction, okay. So there we go, okay, so plastic bottles, right, looks like that, that's plastic bottles.

**00:18:29 - 00:18:33**
And there's cat. That's category, and then there's category name.

**00:18:33 - 00:18:39**
Yeah, and the respective code. I don't know what that one was.

**00:18:39 - 00:18:40**
That would be the product code.

**00:18:40 - 00:18:59**
Probably the category name, plastic bottles. Okay, so this is the sample I'm interpreting, and I could be wrong, that this was an R bill. Okay?

**00:19:03 - 00:19:50**
Yeah, I think any time you needed the product name, that's where it would come from. So it looks to me like it's got a name that says product or whatever it was. If you scroll back up just a bit, where it says plastic bottle, so it's got the name. That would be the product name, then the product code, and then you've got the category, which is plastic bottles and so on. So that's where that information is coming from into the transaction field that you're looking at. It's coming from that area there. That's why it's coming from different places or different APIs, which is why the mapping is so important because the product name will come from the end-of-life products API, but the categories comes from the recovery stream API. Or, sorry, I'll give you a better example.

**00:19:50 - 00:20:03**
Uh, the transaction API, so the shipped quantity comes from the transaction API, so product product code comes from the recovery stream API. The end of life, but shipping quantity comes from the transaction API.

**00:20:03 - 00:20:12**
So what?

**00:20:12 - 00:20:55**
So where you see ship quantity, there ship quantity of product that would come from the transaction API. And the same thing with received quantity. Received quantity also comes from the transaction API. So there are different areas, and I guess that's the key is to understand what it is David needs and is what he needs, is everything he needs in the API endpoints now. And if not, Which additional fields does he need? And then we figure out, OK, are we just missing something and they are there or they actually need to be updated and included?

**00:20:56 - 00:21:12**
So in reality, then. We would need all of these APIs. All of them. To be able to get.

**00:21:13 - 00:21:23**
No, not necessarily. The ones that you're going to develop will just pull from the various API endpoints that we have available.

**00:21:25 - 00:21:35**
So we were looking at the transaction APIs, okay? So these guys here are highlighted in yellow.

**00:21:36 - 00:21:36**
Yep.

**00:21:36 - 00:21:59**
Okay? But if... What you're saying is that a lot of this information, if we only did these APIs, then what I heard from you is that we wouldn't get this R build data. We'd only get a very small piece of this R build data.

**00:21:59 - 00:22:45**
No, you should be able to get all of it. I think. And we'll have to, I guess, confirm with Mark. But they've already gone through and confirmed that what you guys were planning to do is sufficient because you're mostly doing transactional data. So when you have your developer build those APIs, which is why I think it's important to get them involved because I could be wrong. To get them involved, because they may say, well, actually. In order to get that extra information, we also have to develop this one too. I don't think they will, I think they'll just say, Okay, you need a get transaction types, so that what does that mean? It means means that I need to grab like these five fields from the versus API endpoints.

**00:22:45 - 00:23:36**
So that's what they'll do and then they'll develop another one to say okay for, let's say the transaction IDs. They might have to develop something slightly different for that. But then they will map those polls, right, to what David needs in his system. But the first step, I think, is that mapping, is understanding, like, what does David need in NAV? What does Diversys currently have in its APIs? And then we figure out, is anything additional needed? And that may include additional API. It may include just adding new fields to the existing API endpoints, Or it may... actually turn turn out that our team needs to develop a whole new, completely new API for you, all right? And I think that's what Mark and Emma are saying.

**00:23:36 - 00:24:26**
Is like, the sooner we can get that an understanding of that, the sooner we can move on it. And then David will have what he needs. But that mapping, which has been the unknown, I guess up until this point, is what really needs to happen. So David might say, I need information for these like six things. And in this one thing, I need all of this information. So these five or ten fields or whatever happens to be. In this one, I need this. Maybe it's two fields. I don't know. And then we map that back to what Diversys has in its API endpoint and then figure out if something's missing and then either develop it or we just missed it. It's in there. But we did, we just missed it.

**00:24:26 - 00:25:29**
But that's where Mark and then we'll get involved to help with that mapping piece for the unknowns. So when? When you and David say, Okay, I think we can map of the 20, I think we can map 16 of them, but there's these four that are questionable. So let's get the the Diverses team on a call and they can help us figure out this mapping for those items. Or it's missing and they need to take an action. And then that will actually spawn this conversation where you have your API, your selected API development pieces. Because then marking them, if they say, oh, yeah, that's not in there, it's something that we can add to the existing endpoint that you plan on using, or they're going to say, oh, we missed the fact that there's an additional API that your developer needs to add to your list.

**00:25:43 - 00:26:11**
I think that everything that's in the product for the most part should be mappable to what David needs. But that's the unknown. Remember we were talking with Joe, and Joe said, yeah, I think the API document's all good. I understand. I read through it. It's all good. But the most likely scenario is that as he's building it, he might come across like a missing field or something. And that's the same situation with David. He may come across a field that's just missing.

**00:26:13 - 00:26:26**
The one thing I really, really hate about this document, because you've said something today which I've missed, is my inability to see the API overview.

**00:26:26 - 00:26:27**
Right, yeah.

**00:26:28 - 00:27:34**
It doesn't help me. You know, I see this thing that says diverse API, but, you know, me trying to, I've been trying to build this. On my own, but of course I'm not diverse. Is there any way you could send me this, this high level overview in a readable format? I will look into it. Yeah, now that you've said some things. And I went, Oh, wait a minute, maybe I missed that. So yeah, if you could, send that to me. And I can actually, because bouncing through all this text. You know, I'm struggling. I'm really like I'm burning daylight trying to trying to get this organized, trying to get David to understand basically the workflow of diverse. And I'm not being successful because I don't have the information I need. I don't have the visibility.

**00:27:34 - 00:28:24**
I'm not asking to be able to code or anything like that, but. Being able to go okay, I don't even know what this is, I'll make it up. This is the participant API, right? And that's all the categories into there, so the participant API comes down here, I guess, to an end point. So if I need, um, uh, the site information, does it come through here, or does it come through here? Or, you know, because I'm interpreting diverse API in the center here as the endpoints. So if if we need to develop all of those APIS to get the R bill, well, that's a whole different conversation I have to have.

**00:28:24 - 00:28:32**
Yeah, I don't think that's the case, but, you know, I think it's worth a discussion. Exactly.

**00:28:32 - 00:29:00**
So, the more readable information I can get, the better I'll be in a position to smooth the way into, you know, API developments and other things. But I'm struggling here, right? Yeah. And, of course, you know what our meetings are like with David and Mark. Yeah. Very adversarial to each other. Yeah.

**00:29:01 - 00:29:01**
I never know.

**00:29:02 - 00:29:02**
I didn't notice.

**00:29:03 - 00:29:58**
Yeah. So I've been trying to do a lot of. Work with David, trying to get him on board reduces resistance more and things like that. So, yeah, the more information that I have access to, the more visibility, the better off I am at working with David. And I've already knocked off a few of his concerns, but I haven't been able to knock off enough because that's what got us on this conversation. Right, because I was able to easily show them all this stuff, right? But this is where I got nailed to the wall because, you know, I couldn't tell them what this was right. So so, yeah, if if I can get a copy of that, and if you sort of. And I'm lack of the wrong term. But that mapping table we just talked about, if you could share that with me.

**00:29:58 - 00:30:15**
Yeah, yeah, so. But the caveat is that it's unsupported. It's just something that I produce quick and dirty for you. But, you know, I think it might help and it might help to at least like what we just walked through might help to point you in the right direction. So, yeah, I'm happy. I'm happy to provide that. Yeah. Yeah.

**00:30:16 - 00:31:16**
And I accept the caveat that it's not an official document. Yeah. It's like some of the stuff I've created is not official at all. It's just trying to figure something out. So, yeah, I.If I need something official, Duane, yeah, I will ask. I need an official document of XYZ, okay? And then I expect it to be sent in a PDF file and all that other type of governance around it. But working stuff, no, I don't even share the working stuff with Shane, Sam, or David or any team member. So, yeah, it's just to help me get in a better position to successfully educate. The team on things and I haven't, so the conversation we're going to have with Mark. I'm really hoping I've missed something, and I'm really hoping that Molson missed teaching you and I about this. I really hope, because this would be a very big impact, right?

**00:31:16 - 00:31:48**
Yeah, Mark's supposed to join us right now, actually, so I imagine it'll be jumping on soon. Um, but let me just let me just check to make sure he hasn't messaged me. But yeah, I'm, I'm gonna. I'm gonna send you a couple things, actually. I'll send you that table that's just a quick and dirty that I did. Um, I'm also going to send you the release note. Uh, not the release notes, the, uh, yeah, the release notes for the release that just went out on Monday.

**00:31:48 - 00:31:53**
Oh, I thought it was this coming Monday, I thought it was Easter Monday, it was coming out.

**00:31:53 - 00:32:05**
Yeah, no, they just launched it, and the app was released yesterday. So I have the release notes that I just have to put them in a PDF format, and I'll send that over to you straight away.

**00:32:07 - 00:32:19**
Okay, good. So the app on Google Play Store needs an update, right?

**00:32:19 - 00:32:21**
It was approved yesterday, yeah, so it's there now.

**00:32:23 - 00:33:12**
That's weird. I did not get a message to update my app. Just a sec. Nope, I guess Google hasn't released the update because it just searched the Google Play Store and it's not telling me to update, but that's fine. Play with that later. When Mark comes in, it's important that Mark listens to me as I walk him through everything. And when I'm done walking him through, that's when we can step back. Because I want him to see what I, as an operator, operations person, was experiencing, okay?

**00:33:12 - 00:33:13**
Yep.

**00:33:14 - 00:33:19**
And like I said, I'm really hoping it was something missed in our training.

**00:33:21 - 00:33:42**
Yeah, I noticed in the release, too, excuse me, there is a, remember you and I were talking about it, do you think there's going to be additional menu items? So as it turns out, there is. So I need to update the training slightly. So I first need to figure out what that new thing is and how it works. But, yeah, anyway, there's some changes.

**00:33:44 - 00:33:50**
Okay, so we just got the release now. Do we need to push back our training?

**00:33:51 - 00:34:19**
Let me look at how in-depth it may be and how quickly I can turn it around. If I can turn it around quickly, then no. But I haven't had any training on what this new piece of functionality is yet, so I need to figure it out. But I'll let you know as soon as I have a look at it. I mean, worst case is if we just... go ahead with the training so that they're trained on what we have, and then we follow up to cover that one item?

**00:34:21 - 00:34:53**
No, no, no, no. I'm not – no. I don't – when we start bringing the operations team in, I want the product to be in the best state possible and our training documents to be in the best state possible so that they get a good impression right out of the get-go. I'd be much more – confident and comfortable. Pushing back the training, you know, two, three weeks to make sure we are solid before we get the team involved. Okay, all right.

**00:34:53 - 00:35:00**
Yeah. Let me look at how quickly I can turn it around. Because our training is what. Next week, I think, or a week after, we got no.

**00:35:00 - 00:35:01**
Two weeks out, yeah.

**00:35:01 - 00:35:02**
It's two weeks out, yeah.

**00:35:02 - 00:35:06**
Mark, Hey Dev, Hi Twain.

**00:35:06 - 00:36:07**
So Mark, the issue I came across. I'm really hoping it's, uh, something that was done, missed in training, that Duane and I did. Okay, that's what I'm hoping. But what I want to do is I want to show you, uh, what I experienced as an operator. Okay, uh-huh, all right. So I have a transaction here. I'll just go back here, all right. So I'm the operator. Uh, we got this transaction in this, our bill. So I clicked on the R bill, okay? And I looked through it, okay, and I saw all this data and everything else, right? And then I even went a little bit further, okay, and saw this detail. And I thought, brilliant, that's there. But then this particular R bill was selected for QC.

**00:36:08 - 00:37:07**
I didn't see any indication on the screen that this particular transaction was selected for QC. Then I went over to QC, and here's the audit report. Now, ironically, this is the audit report that Molson did with us, Duane. We faked all this, but this is the audit report. And so I have zone twos and a zone one, which means I have some issues. But I can't find in this transaction, this R bill, any relationship to QC or QC adjustments. So if I open up all these down arrows, I don't see anything.

**00:37:08 - 00:37:18**
Yeah, so a couple of things. So I didn't check the IDs, but I assume that this transaction is in the audit report that you looked at?

**00:37:19 - 00:37:21**
Yeah, I can go back there.

**00:37:21 - 00:37:46**
So it's 55F04? Okay. Yeah. Okay, got it. Can you click on that one? Sure. The pet one. Okay. So, and can you, uh, can you expand the pet?

**00:37:47 - 00:37:49**
Sorry. Expand what?

**00:37:50 - 00:37:54**
Expand the product. Uh, if you've got the product, uh, section.

**00:37:54 - 00:37:55**
Okay.

**00:37:57 - 00:38:11**
Can you expand the, the, the pet? I'm clicking. Uh, Can you scroll to the right on that section?

**00:38:13 - 00:38:14**
Oh, there it is.

**00:38:14 - 00:38:28**
Yeah. Okay. So I need to – can you scroll now to the left?

**00:38:28 - 00:38:29**
To the left? Sure.

**00:38:30 - 00:39:35**
Maybe if you make your browser – I don't know if you can make your browser any bigger. No, it's full. Okay. You can hide the menu option on the left. Go down to the bottom right of the menu. Oh, there it is. Yeah, you can hide that. I saw that. Okay, so I think what you're missing is, I'll double check with Mohsen, but I think what you're missing is the next release that we're working on. Because I know I've seen all the items will be showing a status and showing a flag that which ones are in QC. And also the transaction will show that it's gone through an audit and the status of its audit. But I think those have not yet made it into the product. I think they're coming in the next release. So I'll double check with Mosen. But I think that's why you're not seeing what you're looking for.

**00:39:36 - 00:39:37**
Okay, fair enough.

**00:39:40 - 00:39:56**
Also, the audit report that you showed, that's going to change too. We're making some improvements to that. There's going to be a lot more detail in there than there is right now.

**00:39:59 - 00:40:01**
In this one here, this audit report?

**00:40:02 - 00:40:58**
Yeah, so if you were to... Yeah, it's going to change quite a lot in terms of just a lot more detail. It's going to show all of the bags, what the classification of each bag was, rolling that up into the classification of the audit by product. So it's going to actually look at the, rather than seeing the same transaction three times like you're seeing right now, because it's three different audits and three different products. You'll see the transaction once, but you'll see all of the audits that happened within that transaction. So you'll only see one row per transaction, but you'll see all of the audits broken down inside it. So we're changing the layout and putting more details in. So that's going to come in in the kind of July timeline.

**00:41:00 - 00:41:04**
And Duane, we're not teaching QC in the first two training sessions, correct?

**00:41:04 - 00:41:08**
Correct. Yeah. We've made the decision to hold off on that.

**00:41:09 - 00:41:11**
Right. Okay. I just wanted to make sure.

**00:41:12 - 00:41:12**
Yeah.

**00:41:13 - 00:41:14**
Okay.

**00:41:14 - 00:41:51**
Can you scroll to the right again, Dave? I'm not like, you know, I always get confused between. Yeah. Okay. I always get confused between the UI that we've got and the UI we're working on because it's moving so fast and we're doing so much. I just wanted to see if there was a place here. Okay. Got it. Okay. Yeah. So I think definitely what you are asking for, you're definitely going to have in the product. I just need to check the motion as to whether it's the thing that's coming or whether there's somewhere else where it needs to be enabled or something, but I'm pretty sure it's coming.

**00:41:52 - 00:41:53**
Okay.

**00:41:55 - 00:41:58**
Okay. So it's the QC status at the transaction level.

**00:42:00 - 00:42:00**
Yeah.

**00:42:00 - 00:42:04**
And showing the items. Yeah, I'm pretty sure it's next release.

**00:42:04 - 00:42:10**
Yeah, because they need to know, oh, this one got flagged for QC, right?

**00:42:11 - 00:42:20**
Yeah, we definitely, like I said, I know we definitely got that covered, but I think it's in the next, I think it's not there yet.

**00:42:21 - 00:42:24**
Okay, and that's fair. That is very, very fair.

**00:42:26 - 00:42:32**
So, Mark, if it's, If it's in QC, will that disable the claims ready button?

**00:42:34 - 00:43:10**
So some of the things we're adding is we're adding the ability to configure that behavior. So you'll be able to say this cannot move to claim ready until all items have been received in QC, right? You'll be able to set that toggle. Or you might just say, I don't care. As long as I've received it in my plant, I can move that to claim ready, right? We're giving those options. Again, that's all coming in the July.

**00:43:12 - 00:43:23**
Okay, cool. Yeah, because I'm just looking at the claim ready button. So if it wasn't QC and the rule was that you can't submit claim ready until it passes QC, then that would be good.

**00:43:25 - 00:43:25**
That's right.

**00:43:29 - 00:43:31**
Excellent. Anything else to add, Mark?

**00:43:32 - 00:44:18**
No, that was my concern. It was like, what the heck am I missing? Because, you know, we did do the QC portion and all that, and I see it here, and it's like, but I don't see it in the transaction. So how would I know as an operator that something went to QC and there's results? And this sort of goes back to what you and I were talking about, Duane. Is in the transaction history, we need to be able to see that, right? So that the operator scrolls down and went, oh, okay, went to QC, QC report is ready, whatnot. There has to be some method that the operator knows that it's in QC and the QC process is completed so they can start looking at the QC.

**00:44:21 - 00:45:21**
Yeah, so we're going to have a status. We're going to have a status which will be QC completed. Or audit completed. And you'll actually be able to go into the transaction table. So like if you go, if you click on transactions at the top there, the top left. Yep, right there. So you'll have some status here, which will allow someone to filter and see all of the ones that had QC received. QC completed, sorry. So you'll be able to just go, okay, I got a whole bunch of QC completions here. I need to go and review. So that'll come as well. So again, this release has been focused on, I'm coming at it from an audit reviewer perspective. So that's what the audit report is. It's going to show me all the things that have been gone through the pipeline and what the outcomes were. So I can review those and check them.

**00:45:22 - 00:45:23**
Okay, um.

**00:45:23 - 00:46:08**
And we're adding a functionality in the next release which allows you to kind of reject it. So you can say, uh, that I reviewed that QC audit and something's wrong doesn't make sense, so I'm sending it back for for investigation. Um, And you'll be able to. So, yeah, so we started from that perspective. I'm the audit. I'm focused on QC. I'm not focused on our bills. I'm focused on QC audits and I'm making sure all the audits have been done properly. And then in the next release, we're going to kind of say, well, what if I'm coming in just looking at a transaction? I'm looking at an R bill and I want to just see, did that go in QC or not? Right. So I know people calls me up and say, why didn't this R bill get paid?

**00:46:09 - 00:46:36**
I should be able to go in and say, oh, that's because, well, QC is a bit, I know QC doesn't stop you getting paid, but as an example, I could say, yeah, we're going through another recount, we're going through an audit, whatever for that transaction, for that R bill. So you're going to get more of the R bill centric flow versus the audit century flow. So right now it's very much the audit.

**00:46:39 - 00:48:03**
Yeah, while I had you here, I came across a little hiccup this morning and now I forget how. So I'm at the participant level. Oh, I clicked too far down. Sorry, clicked too far down. So I'm now as an end user of Ability Bottle Depot. Because it's all, is this the one? I'm gonna try to replicate the error. It was such a strange error and it flashed away so fast. I have to be fast with my print screen. Where is it? Okay, so it was on 89. It was always pretending to be TAS. Is it this one? Is it 49? Oh, yes. Okay. Yeah, it's 49. It was not 09. We have, in this particular instance, a duplication, right? This is what this flag is.

**00:48:04 - 00:48:04**
Yeah.

**00:48:05 - 00:48:17**
Okay. So it's 349. Except... I don't have any more 349s.

**00:48:17 - 00:48:54**
No, a BOL ID is not the transaction ID. So the BOL ID is your external ID that's maybe written on the paper. So the transaction ID is what Diversys creates. Right. It could be the outbill number, right, most of the time. The BOL ID is like... Something that might be printed on a piece of paper that the driver gives them. So for some reason that same BOL ID got used in another transaction.

**00:48:55 - 00:49:11**
I'm trying to correct it because somebody, I was pretending it was a finger issue. And I'm the admin at Ability Depot.

**00:49:15 - 00:49:17**
You're the admin at the depot. Okay.

**00:49:18 - 00:49:23**
So I should be able to go in and change that BOL ID, make the correction, right?

**00:49:24 - 00:49:28**
It depends on the status. I'm not sure if it's in transit, you can.

**00:49:31 - 00:49:33**
Oh, so I'd have to receive it.

**00:49:35 - 00:50:04**
No, I think you might have to be the operator. You're the depot here, right? Yeah. Yeah, I think, I think once it's in transit, I'm not sure the depot can make any edits because it's in transit. It's like you can't start changing things that are on the truck. Okay, that being said, it shouldn't, it shouldn't have allowed, probably shouldn't. Did you create it through the API?

**00:50:04 - 00:50:10**
No, this is actually one you guys created, yeah.

**00:50:10 - 00:50:11**
But was it created through the API.

**00:50:12 - 00:50:13**
I don't know how you guys created this one.

**00:50:14 - 00:50:28**
Can you scroll down to the comment, to the audit history? Activity by... String? What's that? API. Yeah, it's created through the API.

**00:50:28 - 00:50:44**
Okay. So the transaction was created. So if it's in transit, we can't do anything with this. So it would have to be done at the operator's level. Of the Calgary plant, correct?

**00:50:50 - 00:51:09**
Well, yeah, we don't distinguish between the plants when it comes to the operator. There's only one operator organization, like entity. So can you log in and just see that transaction, see if you can edit it? See how annoying this is, Duane?

**00:51:13 - 00:51:38**
How he has to log out and then re-log in, yeah, because it is one of the items was if it goes. And he assumes, um, like, he basically becomes an alias of the of one of the. The depots he wants to be able to to just go back to into the operator without real re-logging in, so.

**00:51:38 - 00:51:39**
Here's the trends.

**00:51:39 - 00:51:40**
Yeah. Okay.

**00:51:41 - 00:51:49**
I'm now the, at the operator level and I have basically all rights. Okay. So this is the, the one.

**00:51:49 - 00:51:55**
Click on that. Click. And I'm not sure how this, I'm going to experiment here. So I'm not really sure the answer, but click on back.

**00:51:57 - 00:51:58**
Okay.

**00:52:00 - 00:52:01**
Oh, okay. That's the back.

**00:52:02 - 00:52:02**
Okay.

**00:52:03 - 00:53:04**
It's not what I expected. Okay. All right. Can you click on there? Open it again sure uh yeah you can't change those details now what should really happen is i'll take a note i think what should really happen is that. Because this was submitted. So if you created a transaction in the web and you put in a BOL ID that was the duplicate, it would stop you. You wouldn't be able to complete the creation of the transaction. The API is not stopping you from putting in a duplicate. So that's why you have this error. And because you would never be able to create that transaction with a duplicate in the web, there's no reason to edit it. Or we don't give that reason, that ability to edit it.

**00:53:04 - 00:53:15**
But I'll check on, Mohsin's like an expert on this stuff, so I'll check with Mohsin. But I think, I mean, first of all, we shouldn't allow the transaction to be, it should send an error back to the API.

**00:53:16 - 00:54:04**
Okay. Because here was my thinking, okay? If for some reason an R build doesn't, because we have manual depots, right? Who aren't on por so i'm going to create a transaction yeah i guess i can only create oh now bill yeah but i did yeah okay so there's so in here. I created the transaction because I have to do it manually. If that finger happens, I should be able to correct that even after I did all this.

**00:54:06 - 00:54:43**
I think once you've submitted that transaction, the assumption is that it's left. Left the ownership of the depot, right? So now it's on its way, it's in transit. So just them merrily changing things could create an issue. That being said, I think the operator should be able to correct the BOL ID. Because they're deemed as the authority.

**00:54:44 - 00:54:44**
Okay.

**00:54:45 - 00:54:53**
So they understand the ramifications of someone changing a BOL ID after it's already been, you know, on its way, right?

**00:54:54 - 00:55:28**
Right. So as an operator, that makes total sense that I have the authority to make those changes. As a participant, I do not have the authority to make that change. That makes perfect sense to me. What I'll do is I'll do a couple of manual transactions here, create them. You know, try to go in and change a BOL ID, you know, because fat fingers or something, and see if I still get that same error. And then if I do, I'll take screenshots and send it back to you, okay?

**00:55:30 - 00:55:31**
Which error? Sorry.

**00:55:32 - 00:56:08**
So if I have a duplicate BOL ID. Yeah. Because I'm doing it as an operator on the web. Yeah. And if I inadvertently put in a BOL ID that's already used, I shouldn't be allowed to save it. What I'm saying is I'm going to do a couple of experiments. And if it does allow me to save it with the incorrect BOL ID, number one, can I go back in and correct it? That would be the second part of that particular test.

**00:56:11 - 00:56:25**
Yeah, yeah, yeah. Let me just check something because I'm not sure if there's a configurable option on that. You're using ABCRC train? Yeah.

**00:56:26 - 00:56:31**
Yeah, only use that one. Don't use the ops train. Only use that first one.

**00:56:31 - 00:56:32**
Yeah, just looking at the setup.

**00:56:37 - 00:56:41**
Otherwise, Duane's going to have to work a weekend to clean out the ops training environment.

**00:56:41 - 00:56:43**
Yeah, no, don't worry. I'm not going to change anything.

**00:56:49 - 00:57:01**
In the first one, yeah, you can do whatever you want. That's the one that I'm working with POR. Yeah. On the API stuff. I create all my little messes.

**00:57:02 - 00:57:13**
Yeah, no, I'm not going to mess around with anything. Just looking to see if...

**00:57:16 - 00:57:21**
Well, he's looking at that. Duane, you haven't said anything.

**00:57:24 - 00:57:25**
Regarding?

**00:57:26 - 00:57:28**
My camera's working. Oh, yeah.

**00:57:28 - 00:57:33**
Yeah. I didn't notice that when you first jumped on. I was going to say, let's say you got your camera fixed.

**00:57:34 - 00:57:48**
Yeah. Yeah, it was an update from Microsoft to the operating system that derailed. The camera settings. Took me forever to find it and lots of Google search.

**00:57:52 - 00:58:33**
Yeah, so I think the, I think the external reference ID, I'll double check this. I need to check with someone else, but I think the external reference, the BOL ID, is is forced to be unique. In which case, you will you should get that error that when you try to submit it, it will say, you know, duplicate PLID.

**00:58:34 - 00:58:40**
Fair enough. And I would expect that. But what was throwing me is the fact that we have this one here, right?

**00:58:41 - 00:58:55**
Yeah, the API is not handling it the same way as the user interfaces. Yeah. And I think that's why you've got this strange string thing in there. Because I think it's an oversight on the error handling there.

**00:58:56 - 00:58:56**
Yeah.

**00:58:57 - 00:59:07**
Okay, I'll shoot something off to the guys and I'll cc Duane so he can come back to you once we have an answer. Perfect.

**00:59:08 - 00:59:15**
Well, thank you so much for your time, Mark. I did want to bring these to your attention because I just couldn't figure out what was going on.

**00:59:17 - 00:59:43**
No, sounds good. Yeah, keep a track of all of that. I'm sure there'll be more come up, Davi, the more questions or more things that you are not behaving the way you expected. So, yeah, keep a log of those and we can, you know, we can sit and review them, you know, together with Mohsen and, you know. Every week or two weeks, we can just take a look at that list. How do you want to do it?

**00:59:43 - 00:59:46**
Yeah, so Duane is creating the feedback.

**00:59:48 - 00:59:53**
We have that feedback table that's created in Monday. That's exactly what it's for.

**00:59:53 - 01:00:13**
Yeah, so once we actually start getting going and the team's providing feedback and whatnot, then yeah, we'll set up a regular cadence for lack of better term, bug review. So we'll set up a regular cadence once we have the operations team involved.

**01:00:15 - 01:00:25**
Sounds good. Was there any other questions? No. I saw something about the API. Sorry? I saw some email about API.

**01:00:26 - 01:00:37**
Oh, yeah. Duane and I went through that. We're almost at the time. Do you have a few more minutes, Mark? Let me check. Do you want to take this offline with him and try to walk him through what I showed you?

**01:00:39 - 01:00:40**
Yeah, a few minutes.

**01:00:41 - 01:00:41**
Sorry?

**01:00:43 - 01:00:48**
I have a couple of minutes if you guys do. Otherwise, I can talk to Duane later.

**01:00:48 - 01:01:54**
Yeah, well, you can still talk to Duane later. But so this is what I was trying to do. So I'm okay with everything in this upper screen on this R bill. Okay, I can map it. I know what the data fields are and everything else. Where I struggled was in the product area, trying to map what are these data fields? Are they alphanumeric? Are they what they are? Because I'm trying to map it to nav, okay? And using the API document, and I listed the ones that, the categories, This was the area that I couldn't map. I couldn't figure out exactly what this field was. If it's a single field, a double field, alphanumeric, whatever, and I couldn't go back to the API document and figure it out. And that's just everything in this whole product area, not just one. So that's what I was asking Duane yesterday.

**01:01:55 - 01:02:58**
I see. So when you have get transaction details, it's not clear as to what everything is. Okay. I did speak to engineering, you know, as part of our API review. And I've expressed the need to expand on the get transaction details endpoint to be more clear about all of the fields that are provided in the response. So I don't have an ETA as to when that's supposed to get updated. So as soon as I know something, I'll let you know. I think it's going to get treated with... It should be something that's... imminent, but I need to wait for the engineering team to get back to me. It should be something that we should be able to put together in a week or so. Oh oh, it's planned to be updated, but I don't know.

**01:02:58 - 01:03:18**
I've asked them to bump the priority. Okay, so, uh, so, yeah, I don't. I don't think you. Yeah, rather than you bang your head against a wall and try to work this out. Maybe worth waiting, at least until I get an update from the team.

**01:03:18 - 01:03:20**
Yeah, yeah.

**01:03:20 - 01:03:25**
Because if it's going to come out the next week, then, you know, it should explain everything.

**01:03:25 - 01:03:37**
Basically, my time crunch is April the 26th. I have to have the NAV mapping done by April 26th, so okay, that's my time frame.

**01:03:37 - 01:03:59**
Okay, good. Good to know. Yeah, we know we should. That shouldn't be a big deal. Just need to get it. Prioritize it. Certainly. Yeah, no, that should give you everything you need here.

**01:04:04 - 01:04:24**
Yeah, so part of the discussion we had, Mark, was to see that document and then. Figure out what it is that David needs to map, and then make sure that that we have the the field that he requires in order to map to NAV. And that's the next part of the discussion is if fields are missing, we need to know that, right?

**01:04:24 - 01:04:52**
I mean, I guess, I guess one thing that could be done in the meantime is is look at this table and say, you know, what of this table NAV needs, right? So if NAV- Sure, I can answer that.

**01:04:52 - 01:04:53**
I can answer that.

**01:04:53 - 01:04:54**
Okay.

**01:04:54 - 01:05:02**
This is the R bill, and David needs everything that's in this R bill to be sent to NAV.

**01:05:03 - 01:05:13**
Okay. Does he need attachments? No, no, no comment. No audit history, right? None of that.

**01:05:14 - 01:05:47**
Just the last transaction history, and that's what we just talked about. So once it's moved to claim ready, this changes to claim ready. It's that last transaction notification that locks the record and says it's ready to be transmitted. He needs that. He does not need the history of everything that was going on. With the transaction, just that last line. So I'll jump to a claims ready one.

**01:05:47 - 01:05:50**
He needs the line or he just needs to know it was claim ready?

**01:05:51 - 01:05:53**
The status of claim ready, yeah.

**01:05:53 - 01:05:59**
Yeah, because if it's not claim ready, he can't transfer it. He won't see it.

**01:06:02 - 01:06:10**
No, he just needs this last transaction. Why doesn't it show claims ready?

**01:06:10 - 01:06:11**
It does at the bottom.

**01:06:13 - 01:07:02**
Oh, it's right there. Sorry, I missed it. He just needs the date, the time, who authorized it, and the words claim ready. That final field that says, even though the record's locked by me clicking on claims ready, he needs that part of the transmission of that particular art bill. So when he's been talking about status, that's what he was talking about. And I only recently learned what he meant by that word status. I was taking it the same way you were. So he needs this flag of claims ready so that when he imports it into NAV, it goes through the payment cycle.

**01:07:04 - 01:07:09**
Oh, he's going to. Yeah, OK. Needs the flag.

**01:07:16 - 01:07:37**
So Duane and I did talk briefly about maybe in the API we can truncate all the words up here and just leave claims ready, but this part needs to be part of that R bill transmission. So basically everything on the page is part of the R bill.

**01:07:38 - 01:07:52**
Okay, well let's start adding these things to that list so we don't lose track of them should there be. Actually more there. Yeah. And we need to be clear. It sounds like he doesn't just need the status. He needs to know when that status was changed.

**01:07:53 - 01:07:54**
Correct.

**01:07:57 - 01:07:59**
For what reason does he need to know that?

**01:08:02 - 01:09:02**
Compliance of the time that the R bill was approved for payment. So if they don't pay with... I forget what it is. Within a certain amount of days of the ARB bill being finalized, ABCRC is penalized. So now there's a tracking mechanism somehow that says this ARB bill came in on December the 2nd. We have to pay it by December the 5th. And then NAV does its magic and whatnot and issues a check. However, that particular thing does. But if it doesn't get paid for some reason and we get hit saying, hey, why haven't we been paid this hour bill? You know, it was submitted on the 2nd of December. He needs to know that it was approved and claimed ready from Diverse and into NAV on, in this case, December the 2nd.

**01:09:02 - 01:09:22**
So is the issue in NAV? If it is, he has to fix it. But if it comes back that this R bill in diverse was never put the claim ready, well, that's a whole different conversation. So they have deadlines on which they must pay their R bills.

**01:09:24 - 01:09:34**
Yeah, I remember we went through this one and I thought it was something related to the received date.

**01:09:36 - 01:09:42**
Well, for him, right, his received date would be the claims ready.

**01:09:44 - 01:09:45**
No.

**01:09:45 - 01:09:50**
So he won't get it until it's claims ready.

**01:09:50 - 01:10:33**
No, but from the contractual commitment standpoint with the depots, isn't it from the date it's received to getting paid? It might be received at the plant, sit there for a week, no one looks at it, then they move it to claim ready and it's immediately paid. But really, it was sat in the plant for a week. So it's late, right? Anyway, we can, I mean, I just want to make sure we understand what you what the need is there.

**01:10:35 - 01:10:41**
So if you look at this R bill, we have a transaction date, we have an entry date.

**01:10:41 - 01:10:42**
Yeah.

**01:10:43 - 01:10:54**
Right? Yeah. And then the final is the claims ready. So that's when the transaction is created.

**01:10:54 - 01:11:05**
Right? So that's when the R bill is submitted from the depot. Nothing's moved yet. They just submitted it saying it's in transit. Yeah.

**01:11:06 - 01:11:09**
And then we have the entry date of when this art bill was created, right?

**01:11:10 - 01:11:13**
Yeah, which will usually be the same time as the transaction date.

**01:11:14 - 01:11:20**
Right. So in the history of this, the transaction was created, ignore that one.

**01:11:20 - 01:11:20**
Yeah.

**01:11:21 - 01:11:38**
Then the transaction on the 2nd was moved from in transit to receive. So that means we received it here at the plant. And then this, yeah, this is not a very good one. I highlighted. So this one was paused for whatever reason. Right. And then it got moved back to received.

**01:11:38 - 01:11:38**
Yeah.

**01:11:39 - 01:11:41**
All in the same day and then claims ready.

**01:11:42 - 01:11:42**
Right.

**01:11:43 - 01:11:48**
Right. Yeah. So when his claims ready, that means that file is ready to go to NAV.

**01:11:49 - 01:11:50**
That's right.

**01:11:50 - 01:12:09**
Okay. So that the way David explained to me, that's the date he needs to go. That's when his clock ticks is that this is in that batch file. That was posted on December the 2nd. So he has until the 5th to pay it.

**01:12:10 - 01:12:31**
Okay. My understanding was that in terms of your obligation to the depots, it's not from the date you say it was claim ready. Because, again, you saw there you did lots of different steps before you moved it to claim ready. Those steps could take days.

**01:12:32 - 01:12:54**
Right. So in NAV, he only has the one date, which is this one down here, the timestamp of this one that was moved from in transit to receiving. So in NAV, this is the date and time that triggers him. But if he's in NAV and this is happening in diverse.

**01:12:57 - 01:13:10**
That's what I'm saying. I think he needs other dates. If NAV is the one that's tracking compliance with the depots, then I think he needs another date, not the date that it was set to claim ready.

**01:13:11 - 01:13:18**
Good. Let me walk him through this again. And actually, I'm going to record this particular one. This is actually a good one.

**01:13:18 - 01:13:26**
I thought what we were going to do was that the report for compliance was going to come out of Diversys.

**01:13:28 - 01:13:28**
Yeah.

**01:13:29 - 01:13:53**
Because we have all the dates. The only date we're missing is the date the payment was made. So I think we were going to receive the invoice number and the payment date. And then you could track all of this out of diversus. So you know exactly when every step happened and what the intervals were and why.

**01:13:54 - 01:13:57**
So you are expecting data back from NAV?

**01:13:59 - 01:14:27**
I think when NAV, if you go back to the, what did we call them, the events spreadsheet, I think there was an event that said when NAV makes a payment, we need to update the status in Diversys to show that this R bill is being paid. Correct. So, yes, there is feedback. Okay.

**01:14:29 - 01:14:39**
So, you're expecting us to develop an API to transmit the data back from NAV to your endpoint, correct?

**01:14:40 - 01:14:47**
Yeah. Again, my memory is rusty on all of the events, but whatever we've got in the events is our assumption.

**01:14:49 - 01:15:36**
Right, right, right. There are some events. So, Duane, this goes back to our conversation about I'm getting a little bit confused on some terminology that was used. So my expectation was that NAV would be sending data back to diverse, and some of those are going to be the payment date that we're just talking about. So my question always has been the API from NAV. To diverse, you're expecting us to push that data to you, to that endpoint. Or are you guys going to create an API to pull from that? And what I understood was that no. No. Go ahead.

**01:15:37 - 01:15:38**
We're not going to do the pull. No, no.

**01:15:39 - 01:15:50**
No, the way it works, Tav, is you and I were talking about it. There's a get command and a push command. So you either get information from diverses or you push information to diverses. We don't pull anything.

**01:15:51 - 01:16:28**
Right. So you're leaving all the onus on us. So here we go. I have it up on screen. Hold on. Hold on. Because we've had this conversation so many times. Okay. It's one of the reasons why I can't involve my API developers yet. Okay. So we have these get APIs right here, right? So this means that nav is going to reach out through their API to an endpoint in diverse. Pull that and pull that data back into nav, correct? I want to make sure I got my terminology correct.

**01:16:28 - 01:16:29**
Correct.

**01:16:31 - 01:16:40**
Okay. So this post, okay. This is where I'm going to...

**01:16:40 - 01:17:28**
No, no. You can't use get and post as your direction. Get is always getting information out of diversers. You're always getting, okay? That one is easy. Yeah. Post can be used... sometimes to update diverses, but also to pull information from diverses. It's confusing. That's why post is an exception. Because post is an HTTP command. And it can be used both bidirectionally. So in this case, you are actually still doing a get. But the HTTP endpoint is defined as it's a post.

**01:17:29 - 01:18:22**
Okay, so Mark, let me, Let me try this again. Okay, so NAV will reach out for information at the versus endpoints, right? Oh, why did it do that? Okay, that's on these gets, where NAV will reach out. Yeah, yeah, right, so NAV goes to your endpoint. Picks up that information and pulls it back into itself. Okay? The post is where NAV's got to go out and put data, whatever type of data it is, into an endpoint on diverse. Correct?

**01:18:23 - 01:19:25**
No, that's what I was explaining. Not always. Look at that example. You're getting transaction endpoint information. You're getting transaction type configuration. You're getting transaction IDs. Nav is getting transaction IDs from diversus. It looks like it's wrong. It looks like it should be a get. But the problem is that HTTP can be used for different ways. So post can be used to post information, to upload information to a system, and post can also be used to retrieve information. That's why you can't rely on the word post.
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="cc7b952147755acf">>>
</file>
assistant: Already have this one, so I did not re-process it.

Existing file:
`/mnt/obsidian/00_Alfred/10_Diversys/Clients/ABCRC/Transcripts/2026-04-01_ABCRC_Onsite_Calgary_RBill_NAV_API_Mapping_and_QC_Discussion.md`

Send the next transcript.
