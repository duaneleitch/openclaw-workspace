# 2026-03-18 Dav:Duane ABCRC Training and Change Management for Diverse Application

**Creation Time**: 2026/3/18

## Transcription

**00:00:00 - 00:00:01**

Morning Sir, how are you today?

**00:00:01 - 00:00:09**

I'm doing well. Um, I was very happy with the training yesterday from Molson.

**00:00:09 - 00:00:10**

Yeah, good.

**00:00:10 - 00:01:29**

The the product, the the product is much, much, much better than what what we were experiencing, right right? Yeah, um, it's for the longest time it was like, How are we going to use this thing? So it's very nice to see the updates. I totally understand that not all of it's there, and that's fine. That's what releases are for and everything else. So, yeah, I was very happy with what we went through yesterday. And it's a minor concern, but it is a concern. I'm on the sideline of how operation works, right? I don't do it every day. I also don't have the history of how they do everything. And my concern is not really with... the application, it's the concern of how do I break people of old habits?

**00:01:29 - 00:02:04**

Right, right, they're going, they're so used to going in and printing out a report and giving paper copies. And I like the I like how you guys are doing it, where you're forcing much more of a digital environment as to a paper environment. So that's really on our side. That's an operational change that we'll have to go through. But based on what happened yesterday, that was really my only concern is how do I break the operations team? Well, we always did it this way, right?

**00:02:04 - 00:02:09**

Yeah, there's a bit of a change management risk there. Yeah.

**00:02:10 - 00:02:39**

Could you do me a favor, though? I was working on this yesterday. The endpoint verification, right? And just ask Mark, if we clean out the database, does that, because it affects the secret keys, does that affect this endpoint verification?

**00:02:41 - 00:03:25**

Okay, I can check that, yeah. I actually have a proposal for you, Dav. I was thinking about this last night. You know how we were talking with the ABDA group and we were saying we could give you a key now. I mean, I still need to figure out why you can't give them that key, but let's set that aside for a second. But you said we can give you a key now and then you can start to play around with it. And then when we refresh the environment, you're going to basically possibly lose that key and we're going to have to maybe give you a new one. So here's my proposal is rather than clean out this database. Like let's pretend or treat this as like this is your environment and this is the environment that the ABDA group can use and so on.

**00:03:25 - 00:03:47**

And why don't we just create a new, brand new, fresh, clean environment and we'll call it like ABDA dev training or sorry, ops training. And then we don't have to do a refresh of what you have right now. You'll always have this as sort of you can go back and look at stuff if you need to. But we'll have a brand new clean environment for the team to train on.

**00:03:48 - 00:04:46**

Oh, I like that idea. I like that idea immensely, immensely. Because my concern was if we clean out the database, all the learnings and everything that I've done here, I'm going to lose the ability to show Mark and Wilson or you, like, why is this weirdness happening, right? Yep. So if we have a complete fresh environment, then that will actually allow me to set up their accounts ahead of time, walk them through, you know, logging in. The other thing I'm working on is the MFA portion too, right? And sort of get them really solid on just basically logging into the application before we do anything else. So, yeah, if you can make that happen, I support that 100% that will just make both of our lives so much easier.

**00:04:46 - 00:05:24**

Yeah, and then you don't need to worry about ABDA. All they'd have to do is, like, once it works on one environment, you just give them a new key for the new environment. And you're going to have to do that when it goes to production anyway, right? Right. So, I mean, we can give it to them and not impact, like, the work they need to do. They can go ahead and use that key for, you know, from now until whenever, like for the next, say, eight months with no impacts. You won't lose what you've already configured and set up, and you can still go in and play around with it on your own. And then we set up a completely different environment for your ops team, and regardless of what they do and change and so on, it's not going to impact your environment.

**00:05:26 - 00:05:30**

So, yeah, so I've been refreshing this a lot. I still can't do APIs.

**00:05:30 - 00:05:53**

Yeah, I'm going to check that with our QA team today because I did enable it for, sorry, I forget the depot. Turner Valley. Turner Valley. I did enable it for Turner Valley, but it's not showing up for some reason. So, yeah, I still have that as an action item, which actually I need to add to our action item list to cover that off. So, yeah.

**00:05:53 - 00:06:39**

So let's have those two action items then create a –. Proper training environment for AB, for us. I just forgot my own acronym. And then, yeah, I can get the secret key. There was something that was said by Mark in yesterday's meeting that has my head scratching because I don't understand. Yeah. So I understand. Creating a secret key. But Mark said something. So I have a transaction secret key already. That was created by Molson.

**00:06:39 - 00:06:39**

Right?

**00:06:42 - 00:07:00**

And so I can't create a new transaction. This is what I was looking for because I was going to do it right then and there. I can't create a new one. This is where I got confused because it's like, well, I can't see what the secret key is to give to them.

**00:07:01 - 00:07:26**

Yeah, agreed. So what has to happen is because at the operator level, because this is like a key that you use to connect to like nav, for example. Yeah. So the way when Mosin was demoing some stuff, he needed a key to be able to sort of represent what was happening there. And so what you have to do here is you actually have to delete the key that Mosin created and then create a new secret key.

**00:07:28 - 00:08:59**

Okay. I actually understand that part, okay? But this is where it sort of expands. So we have a transaction API key. It's invisible to anybody. Hopefully Molson has it. And I can't demo it because I don't have the API access. And this is a clarification maybe Molson and Mark can give to me. So if I, let me do this again. Sorry. If I masquerade as transporter for Turner Valley, okay, let's pretend I can do an API, right? So I click on the API and I go, and so sort of what they were saying, and this is where I need a little bit of clarification. I will come into here, which is Turner Valley. I will create the secret key for Turner Valley. And in this case that we're having with ABDA, that's the secret key that they need to create their API connection. That's the way I understood it.

**00:08:59 - 00:09:00**

Yes, correct.

**00:09:01 - 00:09:11**

Okay. So what I understood then is that I'll have to get a list of all the depots, and we've got to create a separate key.

**00:09:12 - 00:09:13**

For each one.

**00:09:13 - 00:09:14**

For each one.

**00:09:15 - 00:09:15**

Correct.

**00:09:16 - 00:10:06**

And that's going to be sent to ABDA so that they can create the APIs for each of those depots. Correct. That's the way I understood it. Then that brought me back to our environment, okay, Where I'm the – the way I'm understanding it is that. The Calgary Plant – has to be a participant, and therefore, the API that I need to create for Calgary Plant. To NAV needs to have its own secret key. I like your expression because that's what I had yesterday.

**00:10:06 - 00:10:23**

I'm just trying to doodle it through my mind. I don't think that's the case. Uh, I think it'll just be like that because they're part of your organization or your operation, so I think they would use the same key. But let me let me check on that, for sure. Okay, yeah.

**00:10:23 - 00:10:26**

So you saw the winding path? I went down, right?

**00:10:26 - 00:10:52**

Yeah, yeah, no, no, it's a great question because, yeah, um, you've got the the depot stuff down 100. And like Mark explained yesterday, the reason for that is you can't have one depot. Submitting, uh, you know, uh, submitting, you know, uh, information on on behalf of another one. So that's how we separate them. They each have their own API key, so we know who who are the information is coming from. So right, um, yeah.

**00:10:52 - 00:11:32**

The way I'm understanding is our. If we were live right now, Taz would have to log in as a Calgary plant participant to do the work, and Andre has to log in as the Edmonton plant participant to work. Because everything's done at the participant level, not the operator level, correct? Yeah, and if that's the case, I got to create two APIS, I got to replicate all my APIS, uh, for Calgary and for Edmonton, so I can't just build one API. So that's what I'm now sort of understanding, and I'm not sure if my understanding is correct.

**00:11:32 - 00:11:49**

Yeah, yeah, it could be so when you go to your participants. You're going to have like your depots and then you're going to have your processors or whatever terminology that you use. So each of them may require their own API key.

**00:11:51 - 00:12:04**

Yeah. And here's another annoyance. If I masquerade as somebody else, I actually have to completely log out, log back in. To do the next one, right?

**00:12:05 - 00:12:08**

Right, yeah. Probably because they don't want the information caching.

**00:12:10 - 00:12:32**

Right. So playing around yesterday, right? So we were looking at the transporter of Turner Valley, and then I went, well, wait a minute. If I have to do it for the Turner Valley, and I have to do it for all of these depots, then based on what they were saying, I'd have to do it as the plant, right?

**00:12:32 - 00:12:53**

Yeah. So in that list, and I will confirm this, but in that list, you would have both plants. So you would have the Calgary plant and the Alberta plant. And then you would have an API key for each one of them. Right. And that's how transactions would be created through the API.

**00:12:54 - 00:12:57**

Okay. So I have to duplicate all the APIs.

**00:12:59 - 00:13:12**

So you're going to have one master API key for you as the operator, but then for the transactions and stuff that are coming from each of the plants, they would each have their own API key.

**00:13:13 - 00:13:13**

Right.

**00:13:14 - 00:13:36**

So here's the annoyance part. So right now I'm in as participant ABCRC Calgary, right? So if I'm TAS because I'm a plant and I now want to look at Edmonton, I have to log out.

**00:13:38 - 00:13:43**

Yeah. You have to do that unless you give her operator access.

**00:13:46 - 00:13:50**

Well, no, because I'm operator level access.

**00:13:51 - 00:13:56**

Okay. You can see everything.

**00:13:57 - 00:14:00**

I can see everything. So Taz would have this level, right?

**00:14:01 - 00:14:04**

Yeah, that's a decision you guys have to make, but yes.

**00:14:05 - 00:14:43**

Yeah, yeah. So because she supports both Calgary and Edmonton, she's going to need this access. So this is what I'm trying to get upon. If I'm Taz and I have plant Edmonton, plant Calgary, and I'm doing some work, I've logged in as an operator level, It's the masquerade, which I think is great. So I'm now Calgary. Right. I've done all my stuff in Calgary. I can't go back easily and become Edmonton.

**00:14:43 - 00:14:55**

Yeah, that's true. Actually, can you click on the go back button? It's up on the top there just to see what happens. Yeah. So of course you log in. Yeah.

**00:14:55 - 00:14:58**

It keeps me in as the plant. I actually have to sign up.

**00:14:58 - 00:15:02**

That's what I figured. Yeah. Okay. I'll note that.

**00:15:02 - 00:15:25**

Yeah. Can you ask the question? Maybe there's a functionality reason why it has to be done or something. So I'm talking not at the depot level. I'm talking as an operator because here's my job as an operator, right? So see, I got logged back in as, whoop. I have to verify I'm not a robot first.

**00:15:26 - 00:15:26**

Yeah.

**00:15:28 - 00:15:31**

Wow. Slow. Yeah.

**00:15:32 - 00:16:01**

Okay. So I'm an operator, right? So if I'm trying to check all my depots, or some of my depots or something, and I got a masquerade, there's going to be quite a few depots that they're going to be checking on. But the only way they can do it is through that process of logging out, logging back in, logging out, logging back in, right?

**00:16:01 - 00:16:01**

Yeah.

**00:16:02 - 00:16:21**

So I'm only asking at the operator level, who's responsible for all the depots and whatnot, to have the ability to masquerade and then come back to their operator level. Right.

**00:16:23 - 00:16:33**

Yeah, I can ask the question. It wouldn't be in a June release if it's something that they need to do, but, yeah, it might be something they put in the future.

**00:16:35 - 00:16:44**

Yeah. Ideally, I'd love if it's possible to do this before we go live as opposed to right now.

**00:16:44 - 00:17:04**

That's probably possible. I don't want to speak for them, though. I'll have to run by them and see what's actually involved. It could even be as simple as they do it through Hotfix. It's available in a month. I don't really know. They would have to assess the work that's required in order to make that happen.

**00:17:05 - 00:17:47**

Right. Because I'm okay with right now training Taz and, well, it would be Taz, Andre, and Sharif. It wouldn't be... Because Erin only does Calgary. No, Sharif only does Calgary. So it's actually Taz, the super user, who would need this ability because she supports both plants. Because Andre only supports Edmonton. Sharif only supports Calgary. So basically, two users would need this ability to move seamlessly through. The masquerade process. Yeah.

**00:17:48 - 00:17:55**

Yeah, I can see that being valuable to all customers. So I'm certain it's something that they will take into consideration.

**00:17:56 - 00:18:33**

Yeah. So right now, the fact that they have to log in and out, I'm okay with because I want them to get really solid on the masquerade part, you know, checking the participants and doing all that stuff without a lot of confusion, right? So, yeah. Oh, here's the other thing that I'm sharing with you. Okay. I have two web users. This is rear web users, right? I can expand this to find out who are the two web users.

**00:18:46 - 00:19:04**

So that was you and Taz. Do you see where it has the access? The access column, you see the computer piece? That indicates that that's for the web. So the one that looks like a phone is mobile and that one is the web. Yeah, so that's why you're seeing two.

**00:19:05 - 00:20:03**

Okay, so that's how it pulls it up. Yeah. Okay. So the fact that... DAV receiver is only mobile-enabled. That's why it's not showing up on the web. So in this case, I will have, for Calgary, five web users because they would only be allowed the web. Gotcha. Okay. So what I'm trying to do is retrain my thinking, right? On this, because with mobility, you know how everybody's like, Oh, use our app, use our app, right? Um, in my head, that's by definition a web user, so I just gotta be careful with my own nomenclature there. Okay, thank you for that clarification. Yeah, no.

**00:20:03 - 00:20:13**

Web web means basically you're, you're at a desk and you're you're using the WWW. You know, Https, and mobile is on your phone.

**00:20:15 - 00:22:11**

Okay, so here, and I'm sorry, I don't, due to my other clients and all that, I don't want to give access to my phone to ABCRC's environment. But here's the funny thing. Let me try it again so I can read the message. Oh, where did that T come in? Yeah, see I can access on my phone through Chrome the web and I was able to log in but so that's why I was a little bit Confused so in the per in the user account here If I.If I try to log in as a receiver, I wouldn't get access into the Chrome website. But because I have both abilities.

**00:22:13 - 00:22:17**

You're inheriting the rights from your other user.

**00:22:18 - 00:22:21**

So that's where it got tripped up.

**00:22:23 - 00:22:42**

Yeah, so basically it means, like, you can access it. Like, you're accessed on your phone right now when you're going to, like, to Google and you're going to the website. You're accessing it through the web because you're using a browser. The mobile means you're accessing it through an app that's actually installed on your phone. That's the difference.

**00:22:43 - 00:22:44**

All right, okay.

**00:22:52 - 00:22:58**

Sorry, one is using a native app on your phone, and the other is just using a browser. Right.

**00:22:59 - 00:23:26**

So for our super users that we are going to be training, we'll actually have to train this part because Taz could be on the road, and she'll have the same type of access, you know, bundle or cloud or call receivership or whatever, that if she wants to check details, she can go to Chrome. Go in as opposed to the actual app itself.

**00:23:29 - 00:23:41**

Should we relax at both? But, yeah, we won't include that in this setup training. That's something that we can do separate with whoever the power users are.

**00:23:42 - 00:23:52**

Yeah. So all the training right now is just going to be with the power users, right? So, yeah, it's not. It's not part of the first two training sessions.

**00:23:52 - 00:24:09**

Yeah, that's fair. Well, we can set up a third. So we'll focus on the setup items. Then we'll focus on this main menu items. And if there's specific things that certain users don't need to see and others do, then we can separate those out.

**00:24:10 - 00:25:11**

Yeah, I'm looking for like this particular training, not until like January type thing. Okay. Because this is very specific for a very small group of even the super users. And if I'm clarified, if I'm clear on it, then I have no problem going up to Taz and saying, Taz, you're with me for an hour and I'll show her a demo. You know, because it's very specific. And so what I'm trying to do is replicate what Aaron does, what Taz does and all that. And yeah, some of this, to me, this would not be a diverse training. To me, this would be an ABCRC training because it's specific to our operations. So the fact that Taz needs to have the ability to go into the website when she's driving so her laptop won't start, but she can access it on her phone.

**00:25:11 - 00:25:40**

So if she's dealing with an issue and... you know, she stopped on the road and read there, right. She can use her data and get to the website to get the answers. Yeah. And so that's very specific to ABCRC. And therefore I have no problem doing that type of training because that's pretty simple. I just want to make sure that I'm lockstep with you guys on that. Yeah. So that type of training. Yeah. We don't need to waste your team's time on that one.

**00:25:40 - 00:25:55**

Yeah, and that aligns well with our model. Our model is train the trainer, so we want to be able to train you, make sure you're comfortable and know it so that if you need to impart that knowledge onto someone else in your team, you can do it.

**00:25:56 - 00:25:56**

Right.

**00:25:57 - 00:26:33**

So, ironically, I'm not the official trainer. I'm just, I am the... person who is supporting both Diverse and ABCRC in trying to get this thing launched, so that that's, that's my role. But yeah, there's going to be some more training that's going to be required, especially as more releases come in, but I'm identifying specific training. Matter of fact, let's add this to the action log. Okay, you want to add it? Do you want me to add it? I can add it.

**00:26:33 - 00:26:38**

I have two other items I need to add anyway, so just tell me what you want added and I'll take care of it.

**00:26:39 - 00:27:15**

Okay, so specific super amend users on their ability to use the diverse website on a mobile device. Okay. And assign that to me. And the due date would be, like, January 2027, because hopefully we're going live that month. Or that quarter. So, yeah, so assign that to me.

**00:27:16 - 00:27:16**

Okay.

**00:27:16 - 00:27:17**

Yep, will do.

**00:27:19 - 00:28:10**

Because this will be important for you guys, too. So that's an action item that will benefit. Yeah, because I have to do a road trip up to Edmonton. With the scanner, and that would. Yeah, I'll do a test, I'll stop in Red Deer for lunch or breakfast, actually, and, uh, do the test to see if I can access the website on my phone. Because a couple comments Taz has made in general conversations. Um, that she has to look up things like when she's traveling and all that. So she prints out a lot of stuff, so if I can get her to not have to print out stuff, that. That would be cost savings there alone, right? Yeah. Okay. So that's my test, and then if it works, then I can train her on it.

**00:28:11 - 00:28:14**

Yeah, it should work, no problem. But, yeah, it's worth trying.

**00:28:16 - 00:28:16**

Yeah.

**00:28:16 - 00:28:26**

Well, it works. I'm on my home Wi-Fi, so it works on the Wi-Fi. It'd be on the 5G network that I need to test in the middle of nowhere.

**00:28:26 - 00:28:38**

Yeah, that's the big test is if you don't have connectivity. To your provider, then yeah, that's kind of out of anybody's control, I guess.

**00:28:39 - 00:28:39**

Yeah.

**00:28:40 - 00:29:13**

Okay. So we wanted to talk about the action items. So I went through and pretty much matched up with you on action items, except for this new one. The other action items I have have nothing to do with diverse. So I'm not going to add them to this list here because it's just operational stuff for us here from a project perspective.

**00:29:13 - 00:29:14**

Okay.

**00:29:22 - 00:29:37**

Yeah, that's good. I'm glad to hear that we're aligned. I actually went back like eight months and went through –. It took me forever. I went through, like, all the transcripts. I went through, like, the conversations just to pull all this stuff out to make sure nothing got missed.

**00:29:40 - 00:29:46**

Oh, yes. I just looked that down on my paper. A36 here.

**00:29:46 - 00:29:47**

Yeah.

**00:29:47 - 00:30:50**

The inventory module requirement. Okay. So, yes, I have. I want a working session with you to walk you through it. And especially after what I saw yesterday, because so with what I saw yesterday, I have to be careful because I got to make sure my bias is not going to impact ABCRC. I was asking in yesterday's training session with Molson about a QR code on the pick slip. Remember, we spent a bit of time talking about the pick slip. Yeah, right. And he walked me through how the pick slip is going to work, but in my documentation, the team wanted a QR code on the pick slip. But here's the catch. Because I didn't know at the time. Neither does the team with what Molson showed me.

**00:30:50 - 00:31:51**

Aaron would log into his diverse application in the morning and he would see all these, and so he can do it electronically. So I'm waiting on the pros and cons of this, but I think that's a much better way of doing it rather than printing out another piece of paper. So I was all ready to send you the requirements, but I wanted to wait until we had our meeting yesterday. And so last night I was thinking, well, actually, maybe I should have. A conversation walkthrough of what the requirements are and get you and I aligned. And if necessary, I can take it back to the team and say, team, I removed this requirement because here's the functionality of the application. Right. Yeah. If we're in a better way.

**00:31:51 - 00:31:54**

Then yeah, it's worth investigating.

**00:31:55 - 00:32:17**

Right. And that's sort of what I was talking about, you know, The operational change, because they're so used to doing things a certain way, it might not be the best way now. Sure, it was the best way when they had the system that they had. But now that we have this system, there may be operational changes that we can take advantage of that are cost savings.

**00:32:17 - 00:32:35**

Yeah, and that's the idea. So you notice in the meetings, Merck spends a lot of time really trying to understand. The flow and the process that you're doing today. And he always in the back of his mind, he's like, but maybe we can add value, maybe we can add value by doing this or adding this for you. So right.

**00:32:35 - 00:32:44**

But I'll be honest with you, up until this release. We couldn't see any value of the application, right?

**00:32:44 - 00:33:05**

That's not the first time I've heard that, Dav, and as you know, I've been here like eight months, and you're not the first one to say that. I think there's been similar experience where, like, we're kind of laying the tracks just before the train so the customer doesn't see it until all of a sudden we've got more runway with the track, and they're like, oh, now I see it. Yeah. Yeah.

**00:33:05 - 00:34:00**

So, like, that session I had yesterday was –. So perfect. And of course, I have my executive meeting this afternoon. And so, yeah, it's going to be a change. I didn't really see that there was never any value, but I'm going to be saying a lot more positive things saying, hey, yeah, the train's actually rolling out of the station now. We're on the path forward. Which is actually a good thing because we have a major, major board presentation in April and they wanted more details about this project. And so, yeah, now I actually get to write multiple decks of, hey, this is fantastic. I can see operational changes here that would cost savings, such a reduction in paper and whatnot. So the timing is. Brilliant.

**00:34:00 - 00:34:23**

Glad to hear it. And you're going to see more changes, like Mohsen was talking about some items yesterday, so we're going to do some hot fixes for those immediate bug-type things he was talking about. But the releases coming in June is going to be a lot of additional added functionality that you're not going to see maybe in the UI necessarily, but in the functionality, it's going to continue to go up.

**00:34:24 - 00:34:51**

Excellent. Yeah. Okay, so you're going to add to this sheet, creating a new training environment without any details. And actually, divers can have access to it. But just add my account to it, right, so I can create the end users.

**00:34:51 - 00:34:58**

I will send you the invite and then, yeah, you can add whoever you need to start to prep it for the training.

**00:35:00 - 00:35:03**

Okay. I did have a problem with the multi-factor authentication.

**00:35:04 - 00:35:05**

Okay. Okay.

**00:35:07 - 00:35:24**

However, I'm not so sure it's on your end as opposed to my end, my phone end. Okay. So I'm still working that through, but I'll give you an update next Wednesday on the multi-factor. Okay.

**00:35:24 - 00:35:24**

Yep.

**00:35:25 - 00:36:09**

So I've turned it on. I've turned it off. I turned it on, turned it off. And I'm not sure if there's a conflict with my phone and my multi-factor authenticator. I actually suspect it's my authenticator as opposed to anything on what you guys have done. So, yeah, so still leave me that MFA. I can't find it now because I'm looking at my phone instead of the thing. Where's the MFA component here? Do you know what line it was on?

**00:36:10 - 00:36:19**

I'm going to do a find here, and I'll tell you in one sec. It is 10, line 10.

**00:36:21 - 00:36:22**

Oh, wow, way back there.

**00:36:25 - 00:36:27**

Ah, yeah.

**00:36:28 - 00:36:28**

I hear this.

**00:36:47 - 00:37:00**

Okay, so I misread something. I thought I was behind in an answer for you, but no. That was before it goes into production.

**00:37:00 - 00:37:02**

So I think we've got some time.

**00:37:03 - 00:37:22**

Okay, so I'll give you an update next Wednesday to see if I'm having any real serious problems or if it's just a phone issue because I'm going to also attempt on a second phone. To see if it's just my authenticator. Okay. Yeah.

**00:37:24 - 00:37:24**

Okay.

**00:37:28 - 00:37:32**

So just to recap, I talked about the masquerading issue.

**00:37:32 - 00:37:33**

Yep.

**00:37:35 - 00:38:44**

Yeah. The fact that I can't do the API secret key doesn't appear. That's yours. Yeah. Um, we, we've now agreed that, oh, that's I was about to ask a question. We got sidetracked. So in this particular environment, so you're going to create a new environment for all the training and everything brilliant, and in this environment, um, who am I? I'm not masquerading as anybody, am I? No good. I have to do that. I just lost the question I wanted to ask you. Hold on. So I create the key and turn a value. Right. Right. So you're going to get clarification if I need to create a secret key for both Calgary and Edmonton, or can we use that at the operator level? Yeah.

**00:38:45 - 00:38:50**

I think it's the former. I think you need to create them as participants, and then they each need a key.

**00:38:51 - 00:38:53**

Yeah, so we have to duplicate all of them.

**00:38:53 - 00:38:55**

Yeah, I'll confirm. Yeah.

**00:38:57 - 00:39:49**

But there was something else with that. Oh, finally it clicked in. Mark said, and he said it a few times, but it hasn't stuck in my head. So just hear out my question. So let's pretend this is Turner Valley. I created the secret key and I gave it to Joe. Mark said he needs an account in Diverse. My question is, why does he need an account in Diverse if I've given him a second key? If he does need an account in Diverse, At the participant level, obviously. What role do I give him?

**00:39:50 - 00:39:51**

Sorry, who's Jill?

**00:39:52 - 00:39:54**

Oh, Joe's the...

**00:39:54 - 00:39:56**

Oh, Joe, sorry. I thought you said Jill.

**00:39:57 - 00:40:21**

Oh, no, Joe. So I understand giving Joe the secret key to code into the API. But what I didn't understand is why he would need an account. Because I would have to create an account for them for each of the depot. But what would they need an account for?

**00:40:24 - 00:40:29**

Yeah, I don't know that he would need an account. I know he needs the secret key.

**00:40:30 - 00:40:30**

Right.

**00:40:33 - 00:40:39**

I mean, unless Mark was thinking, you know, give him an account so that he can go in and create the secret key.

**00:40:40 - 00:41:35**

Right. I do not want that. And if that's the reason, then okay, fine, he's not getting that. That's why I kept saying you work through me on this, right? Because I want to set the precedent now with ABDA that when we bring on new depots into the POR system, that they have to reach out to us and say, I need a secret key so I can create the API for depot XYZ. Yeah, that way, the Supermans not only create the separate separate key, but can ensure that the site is set up. Like, that's a whole control feature, right? Yep. Whereas if we give them an account for every depot and they go in and create their own secret keys and everything, it to me, it's a security violation.

**00:41:35 - 00:42:12**

You know, even though they're a trusted vendor, they are not the developers of the application, right? You guys are the developers of the application. So there's a different level of security and support that is recognized in that. But any other vendor shouldn't have access into the information unless we can create a separate ID that the only access that they would have would be to APIs. And the secret key for that depot.

**00:42:13 - 00:42:45**

Yeah, I think if Mark was indicating that maybe Joe needs an account, it was probably because, you know, give me the account. So, like, he's acting as though he works for Turner Valley and that he was the admin or whatever for Turner Valley to create that key. The other reason could be that if he's doing testing and he wants to go into Turner Valley to see if the transaction actually through POR happened, he could go in and look at it. So you could potentially give him viewer access, but not access to create anything.

**00:42:46 - 00:42:49**

So if you can get clarification on that.

**00:42:50 - 00:43:00**

Yeah, if I were you as well, I would talk to Joe and understand what his needs are. If he just needs the key, then. Just send him the key.

**00:43:02 - 00:43:17**

Well, yeah, and I had that conversation with Joe afterwards, and he doesn't see why he would need an account either. Yeah. So that's what got my head scratching. So I said to Joe, I would touch base with you, find out if there's something him and I both are missing.

**00:43:19 - 00:43:27**

I'm thinking that it's just view access. If you wanted to see the transaction in that Turner Valley account, you could see it.

**00:43:28 - 00:43:39**

Right. And if that's the case, then, yeah, that makes sense. But the problem with the viewer is he gets to see everything, right?

**00:43:40 - 00:43:48**

He would see everything in Turner Valley because you would be creating him as a Turner Valley employee. So he would only be able to see Turner Valley.

**00:43:49 - 00:43:54**

Right. But we have to give him that access eventually for every. People, right?

**00:43:54 - 00:44:26**

Yeah, well, if you wanted him to go in and view every, every single one, I wouldn't do that. If he's, if it's just for the build, then, yeah, he really only needs access to one. Because, like we were talking about yesterday, if it works for one, it works for everyone. So right, if he was seeing that, you know, he's pushing a transaction from POR. And it's actually landing in in the Turner Valley, or showing up in Turner Valley. Then that's all he would need to see. And then you would just disable his account afterwards, and in fact, in production, he wouldn't even have an account, right?

**00:44:26 - 00:44:54**

And so that's what I want clarification for. If it's just for for this, you know, testing and everything else, uh, then that's fine, because we're only doing with one, um. But both of us were left with the impression that he'd need a separate account for every depot. Yeah, and I'm like, Okay, this isn't making sense to me. And that's why I say, while you work through me, I give you the secret key. And we work together, right? Yeah.

**00:44:55 - 00:45:35**

If for testing he wanted to see that, you know, that what he pushed actually showed up in Turner Valley, that's the only thing you would need to give to him, and then you can remove it whenever you want. We're doing something similar with NCorp is that their vendors have access to it because they're doing API connections right now, so they want to see that, you know, that what they're sending is actually getting through. And so on. So they have an account, it's a separate account, just like I'm talking about with you, it's like you have one account. They that, uh, that your vendor, like Joe, for example, would have, might have access to it, but that's where he's doing. His testing is testing that in this account, but he wouldn't have access to the other account that, uh, like that, End Corp.

**00:45:35 - 00:45:41**

Is using. So right now, they have two accounts or two environments, which is what I'm talking about doing here as well.

**00:45:41 - 00:45:51**

And and I understand, for testing and all that, but. And then it was like, well, okay, is this got to be done for everybody?

**00:45:53 - 00:46:07**

And in production, he wouldn't have access at all to any of them because then he could go in and look at, like he would have viewer access to go in and look at all those Turner Valley and Calgary, whatever. He'd be able to see it all.

**00:46:08 - 00:46:25**

Right. And so that's what I'm, so I understand during testing and development that access, but what I don't want to do is. Set up a precedent now that once we go into production, this thing will also happen. So I just would like some clarification.

**00:46:25 - 00:46:44**

Yeah, that would never happen. He would never give you vendor access to those sites. No, production for sure, 100%. He doesn't need it. The only time he would need it is for testing. And so if he wanted to see that his transaction made it into Turner Valley in the dashboard, he could see it.

**00:46:45 - 00:46:56**

Yeah, and so I'm okay with the testing, but I've got to figure out how am I going to set this up for a production environment, right?

**00:46:57 - 00:47:43**

Yeah, so the action items, Dav, so I'm going to take them out of this document and put them in. Monday.com, so we'll have an action register there, and we'll track them all from there. That way we can click on, you know, follow-up, or if there's additional information, we can go in and update them, or if we need to assign Mark or Molson to something and get action on it, we can. By the way, I followed up on your ask about the user roles, and Molson sent me a message this morning saying he's going to track down the latest and greatest and send it to me. So once I get it, I'll send it to you.

**00:47:44 - 00:47:44**

Perfect.

**00:47:45 - 00:48:08**

So he had indicated that he thought we sent it. And so as you saw, I marked it as open slash closed with a big question mark because it wasn't certain. And I didn't want to say that it was certain. So I did follow up. He said, yeah, we provided. I said, well, Dab says that we provided one that like a while ago and it's old. He needs the new one. So most is going to track it down.

**00:48:09 - 00:48:50**

Well, so here's the catch to that, okay? The latest security rules I have confuses the heck out of me because it doesn't – so when you get the latest and greatest updated security rules, how about you and I have a meeting and I can explain what I saw on the last document I received? And I'm not sure if – yeah, just get the latest document, set up a meeting. We can walk through it and – Sure.

**00:48:50 - 00:48:50**

Makes sense.

**00:48:51 - 00:48:52**

Yep, yep.

**00:48:52 - 00:48:53**

Okay, cool. We can do it.

**00:48:57 - 00:49:27**

Okay, hold on. Right, okay. I really wish it would stop. My Teams, for some reason, doesn't like it when I switch applications. It turns off my share.

**00:49:28 - 00:49:31**

Yeah, ours does that too. It's finicky sometimes.

**00:49:31 - 00:49:38**

So this is Joe. Do I need to have a phone number in here? Or just the ostrich fields?

**00:49:38 - 00:49:41**

Yeah, phone number is not mandatory, so no.

**00:49:42 - 00:49:51**

Okay. So here's the other question. So here's the roles, right? But I don't have a viewer role.

**00:49:55 - 00:49:55**

Yeah, true.

**00:49:59 - 00:49:59**

Okay.

**00:50:00 - 00:50:41**

So that's what's – because I was playing around with how – I was trying to teach myself, okay, how am I going to – assign the various roles to the team members. And then I went, well, okay, so Sam's going to have access, but he's going to be viewer anyways. And then I went, where's the viewer role? So that's why I was thinking, oh, do I not have the latest update of the security stuff? Like if I now have to give, I don't know, clerical? So that's why I wanted to review the security roles. And I don't think we got the updated one because... some original roles that we've actually been talking about, such as viewers, don't appear here. So what is that viewer role now? Right?

**00:50:41 - 00:50:51**

Yeah, okay, that's, uh, that's good feedback. Okay, I'm surprised it's not there actually, right?

**00:50:51 - 00:51:05**

So, yeah, so you add, so ironically, you added some roles such as QC, but other roles disappeared. And that's what I started going well. There's been a change to the security. So what's the new security?

**00:51:05 - 00:51:10**

Yeah, because like a SAM, for example, like you said, you might only want to give them view access.

**00:51:12 - 00:51:14**

Right. SAM only wants view access, right?

**00:51:15 - 00:51:18**

Yeah. We can't go in and accidentally do something.

**00:51:19 - 00:52:00**

Right. And so if the viewer is now, I don't know, under clerical, that term's not going to work because I need to assign. Clerical duties to people. So that's what I'm trying to do. I have the list of the employees and I'm trying to figure out what role they have access to for future. Right. Cause I got to teach Taz, Andre and Shreve that a new employee or employee who changes job position, this is what we have to do. We've got to switch them from this role to this role or, or whatever. Right. Yeah. Yeah. So, yeah.

**00:52:00 - 00:52:01**

Yeah.

**00:52:01 - 00:52:08**

So, you can use this as a reason to Moulton going, well, Dav and I both can't see viewer.

**00:52:09 - 00:52:13**

Yeah, yeah. I'm surprised it's not there, actually. That's okay.

**00:52:15 - 00:52:15**

Yeah.

**00:52:16 - 00:53:01**

So, that's why I thought there was a change in the roles. And then, of course, yeah, this now makes much more sense. This is mobile, mobile app, as opposed to, yeah. And that's the web. Okay, so, yeah, so I can't, uh, you want to? No, I don't. I'm not doing that until he's, until we get that viewer role. Okay, so see, a lot of good progress has been made with release three. And that's basically what I'm going to be saying to Shane this afternoon. Hey, look, we. We were hurting there for a while, but release three has made a difference. That's why I want to proceed on with the training and all the other stuff we're doing.

**00:53:03 - 00:53:33**

See, the other thing too is I only want to give David viewer access as opposed to any right access because I got to keep him out of this in the aspect that he needs to do anything in here. Yeah, go ahead and take a look if you want to take a look at the data and stuff like that, by all means. But you are not doing anything else. And I'm really trying to keep them out that way, right?

**00:53:33 - 00:53:34**

Yeah.

**00:53:34 - 00:53:35**

Yeah, that makes sense.

**00:53:36 - 00:53:38**

Yeah, there should be a viewer role. Yeah.

**00:53:39 - 00:53:43**

So, yeah, this ain't a multi-nay. That doesn't have the viewer role anymore. Why not?

**00:53:44 - 00:53:46**

Yeah. Yeah, I'm certain it was there before.

**00:53:47 - 00:54:11**

It was, yeah. And then it's disappeared. So that's why I was wondering if there was a security role change based on the previous document. I haven't looked at the document in a couple of weeks now, but I'm pretty sure on the document you sent me there was viewer roles. Well, wait a minute, the viewer role is not there. You know, so what's the new security stuff?

**00:54:12 - 00:54:15**

Yeah. Okay, cool. I'll raise that with them.

**00:54:16 - 00:54:16**

Yeah.

**00:54:16 - 00:54:31**

It's a good example. Like, you know, Sam. Should have viewer, and only once viewer. And David, you know, if he wants to go and look at stuff, no problem. But you know, you don't want to be clicking buttons and doing things that he doesn't really understand. So, exactly.

**00:54:31 - 00:54:36**

Exactly, yeah, so I need that roll back.

**00:54:36 - 00:54:37**

Yeah, what does this button?

**00:54:37 - 00:54:47**

Shit? Okay, all right, so yeah. So we're progressing along nicely.

**00:54:49 - 00:54:50**

Yeah, making a difference.

**00:54:54 - 00:55:23**

Oh, because I'm Turner Valley. I was going to say, what happened to the QC potion? But sorry, I forgot. I switched over to Turner Valley. Let's see. This is what. OK, so now I got to go back to operations. So I got to sign out. As the operator who oversees everything, I should be able to bounce between masquerading and operator without signing out, signing back in.

**00:55:25 - 00:56:08**

For the training, Dev, that you and I have set up for next week, I'm going to try to send you a document in advance. It'll be in draft, so your feedback will be super important. But it's going to cover all of the items that are in the setup. So, like, products, it may not be in that exact order. And the reason is, like you and I were talking about, you have to set up materials before you do shipping containers, before you do products. So I've actually organized it that way so it makes sense. Right. But I am going to cover all of the menu items with the exception of API. Correct. And that's what we'll walk the team through. If there's stuff in there that is going to be handled by the API, I'll just make a note of it.

**00:56:08 - 00:56:25**

We can still cover it and walk through it, but just emphasize that that's one of the API connections so that it's not something they're going to need to do. Exactly. And then just a quick question for you. Rates and incentives. Do you guys actually use rates and incentives?

**00:56:28 - 00:56:31**

You know, I'm not sure. I can ask that question because I'm not sure anymore.

**00:56:32 - 00:56:56**

I mean, I can still cover it and then, but, yeah, what I want to do is focus on the stuff that's actually going to be meaningful to them where they may need to go in and actually set up once in a while and leave the stuff that, you know, that they maybe won't touch just as sort of a nice to know. Because we won't have a great deal of time, so I don't want to waste a bunch of time on stuff that's going to be completely irrelevant to them.

**00:56:59 - 00:57:05**

So rates and incentives. Yeah.

**00:57:08 - 00:57:15**

I think the rest applies, but that was the one question of rates and incentives. Some customers use it, some don't.

**00:57:17 - 00:57:20**

Okay. So what's rates and incentives for?

**00:57:22 - 00:58:11**

So if you actually click on rates and incentives while you're there. Okay. You see where you've got got the R bill set up, so there's a an information. Um, yeah, this is setting up like group rates and stuff like that. So so, if you have like a group of of haulers or that are in a specific area, you pay them a different rate than than another group in another area. You can set it all up here. Yeah, if you have specific rates for, uh, for like, uh, like, maybe you're only paying. This is like somebody that's doing like a hauler that's picking stuff up. Maybe it's a flat rate. Every time they do a pickup, they get paid X amount instead of like how much they have on their truck. It's just a flat fee.

**00:58:11 - 00:58:22**

It's that kind of stuff. I don't know that you guys actually use that, but I'll send you an overview of what it is that explains it.

**00:58:23 - 00:58:23**

Okay.

**00:58:23 - 00:58:29**

Just so you can take a quick look. I don't think it applies, but it may. I don't want to say it doesn't.

**00:58:31 - 00:58:41**

It's not ringing a bell in any way, shape, or form now that I looked at it. So, yeah, so send me the information and I'll investigate for you.

**00:58:41 - 00:59:21**

Yeah, it's going to be covered in that document I'm sending anyway because I'm covering the setup menu for the advanced flow, which is what you guys have. Um, so it's going to cover every section of that, but if there's specific pieces in there that that the team doesn't really know. I'm happy to give them the document as a reference afterwards, in case they want to play it. Play around with the system after we're done the training because it's going to explain. I've set it up, like, what is it for? Um, how do you set it up? And what are the things like, the things you need to keep in mind? So so the nice to knows, or the things to consider with some screenshots and everything through the whole document.

**00:59:22 - 01:00:07**

So everything we cover in the training for them, they'll be able to go back directly to this document and get a complete refresher of what we talked about. Sweet. Okay. So that's the document I'm going to send you. That's the one you and I are going to go through next week on the 24th. Right. And that's going to be how the training is delivered in that order. Yeah. So that way they can be on their systems, and as we're walking through, okay, you need to set up materials, and here's how you set up materials. And then if you've given them that list of, like, the real materials that would need to be created, then they can use that. It's like, you know, Taz, you create one, you know, somebody else creates two, somebody else creates three, that kind of stuff.

**01:00:08 - 01:00:08**

Right.

**01:00:09 - 01:00:30**

And then they can all go in and, you know, click the button on how to add a material and fill in the information and send it and publish it. Then you'll they'll see it all happening live, right? Perfect, which is actually really good, because that's the way I don't learn, right by doing, not by watching. So, yeah.

**01:00:30 - 01:00:35**

And that's why we separated the setup from the operations.

**01:00:35 - 01:01:13**

Yeah, the operation stuff is a little bit more complex. And even for me, so I meant, as we mentioned yesterday, most and I are planning to tag team it. The reason for that is like he's got the the mobile devices, like the Zebra stuff. So if he has to show something on on an app, I don't have that. So I can't, I can't do it. He's got the knowledge of what's actually been built for you guys. So when you're asking questions about, you know, but what about that? And you know what if we have this? I'm not going to be able to answer those questions because I don't know it is as intimately as he does right now, so. So he's going to be there to answer those types of questions that I know I'm not going to be able to answer.

**01:01:13 - 01:01:30**

So we want the training to be worthwhile and not me just taking a bunch of notes and saying, I'll go back to you. But, yeah, that might make sense. Let's do the setup. So then everything will be set up for that actual user training. So here's how you actually will use it in your day-to-day.

**01:01:33 - 01:01:33**

Perfect.

**01:01:37 - 01:02:22**

There's going to be stuff in there like accounts that's in that menu, and it's kind of – it's a bit odd in some senses because, like, some of the setups, the first thing you have to do is set up people's accounts, right? But accounts is not in setup. Right? So there's a couple setup items that are in that top menu that, you know, might be – they may need to go in. Let's say it's Taz, for example, and she's the super user, and they have a new person join the team. She may need to go in and create an account once in a while. Or like you said, if somebody changes roles, she may need to go in and change their permissions. So I think that's why it's in that top menu, because it's something she might have to do more frequently.

**01:02:22 - 01:02:38**

The stuff in the bottom menu is stuff that is like maybe it's once a year, once every six months kind of stuff. Anyway, I'll call all of that stuff out as we walk through it.

**01:02:39 - 01:02:46**

Perfect. Perfect. Well, we used up a full hour this time.

**01:02:46 - 01:02:52**

Yes, indeed. I think we covered a lot of important stuff, though.

**01:02:53 - 01:02:53**

Definitely.

**01:02:54 - 01:03:14**

Definitely. All right, sir. I will let you go. I'm going to put these action items into our action register and make sure that's all up to date. My proposal would be that every time we meet on a Wednesday, we quickly cover if there's any updates, any additional action items, and then move on to other items.

**01:03:16 - 01:03:47**

Okay, perfect. Okay. I'm just re-looking at the calendar here. So we've got the 24th. And depending on what you find out about the separate environment, if we've got the separate environment for training, then we can cancel the application cleanup on the 6th.

**01:03:47 - 01:03:48**

Yeah, I'll switch that out.

**01:03:49 - 01:04:19**

Yeah, you'll find out about the viewer capabilities and why POR needs an account. If it's just for casting purposes, yeah, that makes sense. If there's another reason that I'm missing, I need to know that. So, yes, we've got a training next week. We have our touch point. The week after, we're good. And then, yeah, the week after, we're even better. Excellent.

**01:04:20 - 01:04:26**

All right. We're making good progress, I think. So, yeah, we just got to keep the momentum going.

**01:04:27 - 01:04:29**

Yes, most certainly.

**01:04:31 - 01:04:43**

All right, sir. Thank you very much for your time. And I'll be sharing some information with you, updating the action register, and then, yeah, continuing to prepare the training for our walkthrough next week.

**01:04:46 - 01:04:47**

Perfect. Well, thank you so much.

**01:04:48 - 01:04:56**

Yeah, I will share it in advance. I don't know that it'll be this week that I'll get it done, but probably it'll be Monday, Tuesday at the absolute latest.

**01:05:03 - 01:05:12**

I'm just making some notes for myself so I don't drop the ball on you now that we're actually moving faster. Sweet, sir. So we'll talk later.

**01:05:13 - 01:05:15**

Okay. Cheers. Have a great day. Bye.

**01:05:15 - 01:05:16**

You too.

**01:05:16 - 01:05:16**

Bye.
