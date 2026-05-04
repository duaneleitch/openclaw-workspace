# 2026-03-17 ABCRC POR System and API Integration

**Creation Time**: 2026/3/17

## Transcription

**00:00:00 - 00:01:17**

This conversation is both APIS and AB, APIS and the POR system nothing to do with NAV. Okay, I only want us to focus on, uh, the POR system about to hear it. We will have a future conversation about NAV, but I really, really want to focus on APIS, uh, and POR. The other thing, too, is because of the game plan I develop. Um, I want to be careful about when we do the POR connections. I need my operations team solid in the whole manual process. Okay, um, so I'm not looking for the POR API connection until don't quote me on this. I do have it somewhere. Um, but, like, May, okay, so um. Until then, I really want our operations team to focus on the setup and manual operation parts. Okay? All right. So, with that being said, Mark, you're on mute. Hi, Laura. You're on mute, too. Where should we begin?

**00:01:18 - 00:02:05**

So I got a note from Laura yesterday reminding me that I'd already received the Swagger API endpoint for this. It's at training.diversuspro.com. I assume that one's still probably the valid one, so we can leave that aside. I can forward a note separately beyond that. The only thing I need is API keys that will work in that training environment. With respect to the deadline that was just mentioned around – kind of pushing the operations people until May. We won't need any support in the short term, and we won't poke anybody in the eye trying to get additional information. But if we have the API key today, then we can start planning and doing development on our own side. I can't imagine there being – we've reviewed the API documents before.

**00:02:05 - 00:02:14**

I can't imagine there being anything we even need support on outside of maybe a missing field or two, and we can deal with that once your operations stuff is all straightforward. But we're just looking to get that API key.

**00:02:15 - 00:03:02**

Yeah, let me jump in there. OK, so so I can give you the API key right now. OK, however, however, with this being in mind and Mark, correct me, but this environment that you're going to access is going to be undergoing a complete cleanup on April the 6th. So basically. Everything's going to be wiped, removed from there, with the exception of myself and Molson's ID, because we need a clean environment for our operations team. So, Mark, if I wipe this, this database or the environment, I would have to generate a new key for them, correct?

**00:03:04 - 00:03:46**

Yeah, definitely a new key. Because you'd need to recreate the depot, and you recreate the depot, you need to give them a new account and a new key. But there's also things that would fail when you try to create the transaction through the API, because it requires that the right configuration is in place. So the products need to exist, the carrier needs to exist, the ABC or C as the receiver needs to exist. So if you've got a completely blank, uh, you know, database, then yeah.

**00:03:46 - 00:03:56**

So let me ask you this question, Joe, how much time do you need to develop the APIS? Are we talking months? Are we talking days, weeks? What are we talking here?

**00:03:56 - 00:04:32**

I think it's not going to be necessarily that length of time. I'm not sure of the amount of total development time, but we're going to be scattering it across a number of other projects. We have other priorities as well, and so we're trying to basically slot it in when we have a moment. And so for me, knowing that the access, like knowing that individual API calls might fail, for example, is something that I can work around when we're doing our basic testing here because all we're really trying to do is submit the ER bills. Manually and do a couple of other basic API calls. Once we hit May, we can be a little bit more specific about it and say we need this to function fully.

**00:04:32 - 00:05:08**

But if I, if I know a call looks like X, and when I invoke the call, it says there's missing data on the back end. I can put that aside and deal with it in May again. So I guess my objective here would be to get to get the keys as early as possible. We don't have, if we had to get another key again, like we don't have to have this larger conversation again, we can basically, even if, whether you want to do it electronically or online, however we do it, it doesn't have to be another conversation. So we can, we can exchange keys as often as we need to. We're just looking to get access to the API. So we have a place where we can do sanity checks against the calls that we're making, as opposed to being completely in the dark on them.

**00:05:09 - 00:05:34**

Okay. So the good news is it's just me. You have to deal with. So at any time, if you need a new key, you just reach out to me and say, hey, I need a new key. And I'll keep you up to date with what we're doing in regards to the database. But Mark decided to surprise me with something. Mark, I have an AIMCP. What is that?

**00:05:37 - 00:05:38**

What are you looking at?

**00:05:38 - 00:05:40**

Oh, lost my screen share.

**00:05:48 - 00:05:49**

Oh.

**00:05:49 - 00:05:57**

Yeah. So I take it I'm not to give him that. No. And.

**00:05:59 - 00:06:02**

Is that MCP from like the movie Tron? Yes.

**00:06:03 - 00:06:04**

Awesome.

**00:06:08 - 00:06:12**

I think there's a bunch of old men on this call is what I'm getting the gist of.

**00:06:14 - 00:06:42**

No, actually, surprisingly, it's a very, very modern term. It's the, what you call it, and I forgot the acronym, what it means, but it's basically a connector for AI, for an AI agent. Okay. So I forget what you call it now, connector protocol or something. So that is actually an API which allows our AI agent to, uh, connect. Okay, so would Joe be an Abda?

**00:06:42 - 00:06:47**

Yeah, so would Joe be an Abda? Do I say transaction?

**00:06:47 - 00:06:49**

Okay?

**00:06:49 - 00:06:54**

Where did transaction go? That's right, very hesitated one.

**00:06:54 - 00:07:01**

Because you already got one created? Probably. Yeah, you do. You got one, That's fine. You can only have one at a time.

**00:07:01 - 00:07:04**

Oh, you're right, Molson created that, um.

**00:07:04 - 00:07:07**

And you have to create it as. The depot.

**00:07:11 - 00:07:14**

So individual depots for them, right? Right.

**00:07:15 - 00:07:17**

Because each depot is going to have a separate key.

**00:07:19 - 00:07:21**

So I don't get a generic key.

**00:07:22 - 00:07:31**

Yeah, because the key authenticates who the depot is. Right. So we can't have depots submitting transactions on behalf of other depots.

**00:07:32 - 00:07:41**

Okay. So for every depot, We need... secret keys, okay, um.

**00:07:41 - 00:08:03**

Which is which is done by the. You have to log in as the administrator of that depot, so the main participant account of the depot. And there'll be a menu option for them to create an API key and you, you're creating the transaction one, right?

**00:08:03 - 00:08:57**

So, I forget how many depots we have. I mean, we have more than five, that's for sure. Joe, how many keys would you want to start with? Keeping in mind that April 6th, everything gets wiped out. Just one's fine. Just one? Okay. I think I got depots I can do. I'll just add myself to that. Okay. And this is a good refresh for me because it's been so long since I did it. Okay. Yeah.

**00:08:58 - 00:09:00**

Okay. Okay.

**00:09:02 - 00:09:28**

So what I'll do, Joe, is in a separate. Uh, phone call, uh, non-recorded. Uh, I'll create the secret key and give it to you. Um, yeah, we'll use Turner Valley. Um, I gotta, gotta add myself to it. As a people, people amend, correct? Mark?

**00:09:28 - 00:09:34**

Yeah, you have to look at the administrator for the depot. Yeah, okay.

**00:09:37 - 00:09:37**

All right.

**00:09:37 - 00:10:03**

And you should then see, you should see in the setup, when you're logged in as that administrator, you should see in the setup menu at the bottom, APIs. All right. If you don't see the APIs, then for some reason, then I'm sure Duane can help you set that up. I'm not sure it's enabled by default.

**00:10:10 - 00:10:16**

Okay. Yeah, I got to think about this. It's been so long since I did it. Just review how I add myself into this depot.

**00:10:21 - 00:10:43**

You should be able to... What do you call it? What's the term, Duane? When you masquerade. You should be able to masquerade. As a depot from your operator admin. Right.

**00:10:44 - 00:10:45**

I'm trying to remember where that is.

**00:10:48 - 00:10:51**

Are you logged in as the administrator and the operator?

**00:10:52 - 00:10:54**

At the operator level, yeah.

**00:10:55 - 00:10:57**

Yeah. So click on the participants tab.

**00:11:01 - 00:11:01**

Oh, there we are.

**00:11:02 - 00:11:08**

Yeah. Then click on the right icon. And now you can masquerade.

**00:11:09 - 00:11:12**

Yeah, it's been so long since I did that.

**00:11:12 - 00:11:15**

There we go. Then click on setup.

**00:11:16 - 00:11:16**

Yeah.

**00:11:18 - 00:11:30**

All right, so APIs are not enabled for those participants. Duane?

**00:11:32 - 00:11:35**

Yeah, I'll take a look at it.

**00:11:35 - 00:11:39**

Yeah, if you can help. After that, I think it would be good.

**00:11:42 - 00:11:49**

Now that that's been refreshed, yeah, I totally forgot about the masquerade. But yeah, I can get this way and get the API once I see it in the menu.

**00:11:49 - 00:11:49**

Yeah.

**00:11:50 - 00:12:19**

And then I can share that with you, Joe. Sounds good. Yeah. So at any time you need something like that, just reach out to me directly, Joe. If there's anything else you need, like make something up. The endpoint's not working on diverse. Well, then we can reach out to Mark and say, hey, Mark, this little hiccup happened, okay? Sounds good.

**00:12:20 - 00:12:50**

Yeah, and again, the way that we're working DAV is that during any kind of integration support that Joe and Laura are doing, then if you've got any questions or something's not behaving, you can raise those with Duane. Sometimes it's just about explaining things. And then Duane will bring it to product team if there's something that's unusual or isn't working as expected or we've got a gap that could be there.

**00:12:51 - 00:12:58**

Yeah, I always reach out to Duane first and say, can you answer this? Or then he says, oh, no, invite Mark to the meeting. I go, okay.

**00:12:59 - 00:13:00**

Sounds good.

**00:13:01 - 00:13:37**

Yeah. Yeah. Okay. Well, on that note, I can let you guys go. I'm sorry. Do you have any other questions, Joe? Not for me. No. Laura? No. And you missed my explanation. So we have a Laura Nelson at ABCRC. And I sent the email to her and she was on vacation. And when she got back, she notified me that I don't think this email is for me. And that's when I realized that I accidentally sent it to the wrong one. That's why things were late.

**00:13:38 - 00:13:43**

There's two of us, I'm afraid, for the future of humanity.

**00:13:44 - 00:13:59**

Oh. Okay. So, yeah, so I guess I can let y'all go. Give you back 15 minutes. Thank you. Great. Good luck with everything. Thanks, guys. Thanks.

**00:13:59 - 00:13:59**

Have a good one.

**00:14:01 - 00:14:05**

Duane, you want to hang out? Yeah, sure. Yeah, sure, man. Sure.

**00:14:05 - 00:14:05**

Sounds good.

**00:14:08 - 00:14:49**

I forgot how to masquerade, so that's kind of funny. It's been so long since I did it. So, yeah, so I'll need the API enabled in the participant level. Yep. I was working on your document and I came across something. A-087. Yep. The roll table. Yes. The roll table that you shared, well, AB or diverse shared with me was very old and it doesn't actually match the new reality. So do you have a new table? That's what I need to start.

**00:14:50 - 00:15:07**

Yeah, that's good information. That's what I wanted to check was because Mohsen's comment was, I think we already gave this to them, but I was like, I'm not sure that we've given them the updated one though. So that's why I simply called that one out for you to confirm because he seemed to think we already gave you a new one and I wasn't so sure.

**00:15:08 - 00:15:19**

No, I did double check because I've been waiting on it because in my case, I have to go, okay, this is a TAS. This is an errand. So I can create their IDs, right?

**00:15:19 - 00:15:20**

Right.

**00:15:20 - 00:15:27**

And so the last one I have, yeah, there's only like two or three roles. I can't remember. So, yeah, that I do need.

**00:15:28 - 00:15:44**

Okay. I will follow up with Mohsen on that. But, yeah, that's why you see I left it open slash closed because I wasn't sure. So that's the whole purpose of going through this. Right. As far as the APIs go, you wanted that for Turner Valley, correct?

**00:15:46 - 00:15:47**

Yes.

**00:15:47 - 00:16:15**

Okay, so so I just enabled that down, so if you if you check now in Setup you should, or in Settings, you should see. Right? I hope no, see it. Okay. No, yeah, so turner, let me see, it's, it's enabled. Uh, save, maybe I didn't save it. Try that.

**00:16:15 - 00:16:19**

I didn't realize you had this access level now. About time they gave it to you.

**00:16:19 - 00:16:26**

Yeah, yeah. I have to go through this with Mohsen to make sure that I have all the right access for the training.

**00:16:27 - 00:16:34**

All right. Click on settings.

**00:16:34 - 00:16:36**

Jeff, just to see.

**00:16:38 - 00:16:42**

Yeah, there's settings. There's setup.

**00:16:42 - 00:16:43**

Okay, weird.

**00:16:52 - 00:16:53**

Yeah.

**00:16:53 - 00:16:57**

Okay, I'll look into that. I'll look into that further because I did just enable it.

**00:16:58 - 00:17:06**

I didn't realize we need – I forget how many key posts we have, but I didn't realize we need a separate API. So that's good clarification.

**00:17:06 - 00:17:15**

Yeah, yeah, each one needs its own API. This, as Mark said, so that one depot is not submitting transactions on behalf of another.

**00:17:16 - 00:17:16**

Right.

**00:17:17 - 00:17:24**

Yeah, they all need their own. So every depot you set up, you'll have to go in and enable the API and create a key.

**00:17:26 - 00:17:44**

All right. Yeah, I made a highlighted note that I'll put onto my action board. So that could be actually part of the whole training. So when you put in your site, you've got to create the API key.

**00:17:46 - 00:17:50**

Yeah, that's for the API stuff.

**00:17:50 - 00:18:05**

So we had talked about not covering API as part of the training. So I don't know if you still want to go that route or like in just you and I.Talk about API. We can create documentation around that that you can share with the team. Do we actually cover it?

**00:18:07 - 00:19:09**

All right. You're still on the same path. APIs are not to be discussed with the operations team. So that's what I'm saying. If there's any API stuff, I will do it. So really trying to, how do I say this? Trying to keep the technology portion out. Of the conversation with the operations team until we're solid and that, uh, you know, once we start on the NAV side. And an API has to be created because I already created the documentation on how to create a key. Um, but I did that at the uh, operator level, not at the depot level, so I'll adjust my documents to that. But, uh, Shane and I had a conversation. We're going to limit. API creation to one person with one backup. So anytime an API key needs to be created, they have to reach out to this one person or their backup to get it created. Right.

**00:19:09 - 00:19:12**

Yeah. That's the right approach for sure.

**00:19:13 - 00:19:28**

Yeah. And we do not want it to be David. And so Shane's going to, as we get further along the lines, Shane's going to give me the two names of who I need to train on the API creation. And that's all we need to do.

**00:19:29 - 00:19:35**

Yeah, we can put some documentation for them around that, a little short how-to, if you will.

**00:19:36 - 00:19:37**

Yep.

**00:19:38 - 00:19:43**

Because it's not something they're going to go in and do every day, so it's nice to have that fallback.

**00:19:48 - 00:20:16**

Yeah. Something's going on with the database. Oh, there we go. So this is me. All right. I got to think of how I get to this again. It counts.

**00:20:19 - 00:20:24**

Nope. That should be a participant's tab there.

**00:20:27 - 00:20:39**

Oh, right. I keep forgetting about that tab there. Nope, still not showing up. Okay.

**00:20:40 - 00:20:49**

Yeah, because I did check your – and it does – I did enable the transactions API for Depot, for that Depot.

**00:20:50 - 00:21:04**

Okay. Well, let's give it a little bit of time. Yeah, we can touch basic first thing tomorrow morning if I have the API there or not. It's not like Joe's going to do anything with it right now.

**00:21:04 - 00:21:17**

Yeah, I'm going to look into it in the meantime just to see because it should have been instantaneous. And then, yeah, you can give Joe the key and he can play around with it for a few weeks. And then if we have to create a new default and give him a new key, then it's not a big deal.

**00:21:19 - 00:21:24**

Yeah, because he only needs one. Yeah, that's the nice thing.

**00:21:24 - 00:21:28**

Right? If it works for one, it works for everyone. Exactly.

**00:21:30 - 00:21:36**

All right. All right, sir. So I'll touch base in our meeting tomorrow, let you know if I got the API thing back on Turner Valley or not.

**00:21:37 - 00:22:00**

Okay. Yep. Very good. And yeah, we'll cover the rest of that action item list. So I will look into, I'll respond to most and saying, and I don't think we provided the latest and greatest. So let's see if that's okay. Yep. I'll see if I can get that from him. All right, sir. Perfect. Yeah. Thank you very much. Have a great day and we'll chat tomorrow. You bet. Okay. Bye.
