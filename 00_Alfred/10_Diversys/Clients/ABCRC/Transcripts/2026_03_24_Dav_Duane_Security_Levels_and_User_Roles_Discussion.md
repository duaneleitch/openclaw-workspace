# 2026-03-24 Dav:Duane Security Levels and User Roles Discussion

**Creation Time**: 2026/3/24

## Transcription

**00:00:02 - 00:00:19**

So, before we get into the training stuff, can we talk about the security levels? So, yes, this is a brand new document, by the way.

**00:00:20 - 00:00:23**

Okay, so you haven't seen this one before. Okay, good.

**00:00:25 - 00:00:29**

What did I do here? Oh, something like that.

**00:00:37 - 00:00:38**

Huh?

**00:00:38 - 00:00:41**

There we are. Okay.

**00:00:44 - 00:00:58**

So you guys have a viewer level here as the operator. Can you explain your thinking about not having a viewer at the participant level?

**00:00:59 - 00:01:02**

I cannot. I ask the same question.

**00:01:04 - 00:01:06**

You're on mute. Oh.

**00:01:11 - 00:01:25**

Yeah. Sorry. I thought it was off mute, but it went on mute. Okay. Yeah. So I can't explain why. I did ask the same question, though, Dab. So TBD, I'll get back to you when I know.

**00:01:27 - 00:01:27**

Okay.

**00:01:29 - 00:02:13**

Because ironically, in all of our security conversations, it came. It kept coming back. The use cases for the viewer at the operator level is also the same use cases at the participant level. Because we don't want to depose the ability to assign viewers security if the viewer has... It's only at the operator level. So whether you call it another name or something, we would need that security functionality at the participant level.

**00:02:13 - 00:02:27**

Yeah. Yeah, I've noted that. So I have it on my to-do list to create a ticket. So I asked the question to the product team, didn't really get an answer. So I'm going to create a ticket for it, and then we'll see where it goes.

**00:02:28 - 00:02:35**

Okay. Explain this one, advanced and basic modes.

**00:02:37 - 00:02:39**

Sorry, which one are you looking at?

**00:02:40 - 00:02:46**

I'm highlighting this line five here. It says available to both advanced and basic modes.

**00:02:46 - 00:03:10**

Yeah, so we have basically when we're doing setup for the tenant, if they're using the basic flow like what CalRecycle is using, then that's what we enable. If there's advanced functionality like what we're building for NCorp and ABCRC, where there's compaction and QC and shipping or inventory, that's all in the advanced module.

**00:03:11 - 00:03:12**

So that's in the tenant.

**00:03:13 - 00:03:16**

Yeah, yeah. It's set at the tenant level.

**00:03:16 - 00:03:18**

Not app. Okay. Yeah.

**00:03:19 - 00:03:40**

So when we're working, so you know when Mark and company were working with you guys in the early days and they were trying to understand your business and your workflows, et cetera, that determines whether you fall into the basic flow and we can manage it there or if you need the advanced functionality. So in your case, it's the advanced functionality. So it's a more advanced setup.

**00:03:43 - 00:03:47**

Gotcha. Okay, so it's the tenant. Yeah, it was like, wait a minute, there's two levels in here? I'm getting confused.

**00:03:48 - 00:04:07**

Yeah, no, no. The basic model is basically everything you have includes a basic model and then some. So you have the advanced functionality. So when they set up your account, just like the new account we set up, it's basically enabled for the advanced functionality.

**00:04:09 - 00:04:33**

Gotcha. Okay, that's good. So the other thing, the masquerade capabilities, as I'm trying to do stuff, right? So I go to the participant and then I masquerade, right?

**00:04:34 - 00:04:34**

Yeah.

**00:04:35 - 00:05:42**

It becomes confusing, even for me. Where I have to keep exiting out and coming back in, exiting out, coming back in. And so, yeah, we really need the ability that on a simple masquerade, not a simple masquerade, but on the masquerade, the operator, because it's going to be at the operator level, right? Yeah. Has the ability to go in. Check whatever, and then come back. But here's the other thing. If you saw, I'm masquerading as Turner Valley, right? So if I'm masquerading as Turner Valley, how come I'm seeing Ability, Calgary, Bottle Exchange? Like, why am I seeing all these transactions? If I'm masquerading as Turner Valley.

**00:05:42 - 00:05:50**

Right. Good question. You should only be seeing Turner Valley transactions.

**00:05:51 - 00:06:01**

Right. Right. Okay. So I'm not misunderstanding it. It's just there's a quirk that I found, or bug, whatever you want to call it.

**00:06:08 - 00:06:21**

Yeah, the idea is that it's basically compartmentalized so that Turner Valley, you only see their transactions and then you go into like Alberta bottling and you only see their transactions.

**00:06:23 - 00:06:48**

Right, that's what we're supposed to do. So, yeah, so if I masquerade right here, Turner Valley, or let's even masquerade as Ability Bottle Depot. Log you out and log you in as the admin. Which is fine. I'm the men of ability. But this one, I only see ability.

**00:06:49 - 00:06:51**

Yeah, that's what you're supposed to say.

**00:06:52 - 00:06:59**

Right. But why when I went in as Turner Valley, is it because Turner Valley is a carrier?

**00:07:00 - 00:07:05**

Yeah, it could be. I'll have to check into it. I don't know the answer offhand, but I can look into it.

**00:07:06 - 00:07:12**

So then that creates a problem for me. Oh, hey, it came up. Yay!

**00:07:12 - 00:07:12**

Yay!

**00:07:18 - 00:08:38**

Yeah, so I'm going to have to create a new secret key. So because of what we're trying to do with POR, we're going to use Ability Depot when we set it up, okay? Because a carrier would not be doing anything on the POR level. True. So I'm going to be doing it to ability, and I forget what day. It was last week sometime. I came in here to see if I could do an API, and it wasn't here, so I was about to ask you to enable it for all, but I guess it just took time to get through the whole system. So I have that ability now, which is great. Okay. So. Yeah, if we can get clarification on that, that as a carrier, see how annoying this is? Yeah. Yeah, as a transporter, do they see everything?

**00:08:41 - 00:08:46**

Can you go in there for a gun down? Just quickly. Sorry, I know it's going to make you log in and out again.

**00:08:46 - 00:09:14**

Yeah, no worries. Okay, so this business, Turner Valley, is a carrier. So masquerading as the carrier, I see all transactions. Okay. What did I hit? Oh, because I'm the carrier, so in the carrier level. Yeah, that's why it appears, right?

**00:09:14 - 00:09:23**

Yeah, because the shipper is, uh, ability or, uh, Calgary or whatever. And and you're picking up from those locations, yeah, that's why you're seeing it, right?

**00:09:23 - 00:09:31**

So, So the question I have. You're the between.

**00:09:31 - 00:09:34**

You know, the shipper sending it to the, carrying it to the receiver.

**00:09:35 - 00:10:31**

Right. So the curiosity question I have, as a carrier, how would I use the transaction section? Like, I don't see myself, if I'm a truck, taking bottles from the depot to the plant, why would I need to know this transaction? I guess I'm asking why, if I have a carrier, why would they be able to see? Why would we put a carrier? Give access to a carrier into Diverse. What's the business purpose of giving a carrier access to Diverse?

**00:10:32 - 00:10:49**

If you wanted them to see their transactions, so all of the pickups they did from who and delivered it to whom, you could do that. I think there's also a setting, though, that you can give them access just to the mobile and they don't have web access, so then they wouldn't be able to see the transactions.

**00:10:52 - 00:10:53**

Right, so if I give them all.

**00:10:54 - 00:10:58**

Yeah, so that's a business decision of whether you actually want them to have web access or not.

**00:10:59 - 00:11:14**

But where I'm struggling before I make the recommendation to Shane, where I'm struggling is understanding why would it give a carrier web access to see transactions?

**00:11:18 - 00:11:24**

Unless they're submitting. Claims for payment for all their deliveries.

**00:11:26 - 00:11:35**

Okay. So they're going to submit claims. All right. What is claims again?

**00:11:38 - 00:11:58**

So this is where they would put in for that transaction, they would put in all of the items that they're claiming. There could be things like, Uh, you know, we were briefly discussing, like whether you're going to pay for fuel surcharges and things like that. They can make that all part of their claims. I don't know if you guys actually use claims, though.

**00:11:58 - 00:12:10**

Yeah, I don't think you do. Um, no, it's. It's like the other thing, this, uh, oh, it's not on this one. Forget what it's called rates and something. Uh, we're trying to figure that all out.

**00:12:10 - 00:12:12**

Yeah, incentives, yeah.

**00:12:18 - 00:12:20**

So I'm Turner Valley.

**00:12:20 - 00:12:48**

Yeah, because the rates and incentives is really a special setup. So like if you have people that are all in a region and maybe you're paying them more money because like let's say they have to travel much farther to do those pickups. So you're giving them some sort of a stipend or whatever for additional fuel charges to do that extra travel, like things like that. So maybe there's a group that gets paid slightly more money. For doing pickups than other groups.

**00:12:49 - 00:12:50**

All right.

**00:12:53 - 00:13:12**

So the reason why I'm asking these questions is it's related to the security rules, right? So Turner Valley, which is a carrier, is that the hauler shipper?

**00:13:15 - 00:13:20**

It's the hauler. The shipper would be the depot, and the receiver would be your facility.

**00:13:22 - 00:13:29**

Okay, so is that a driver then? The carrier is the driver?

**00:13:30 - 00:13:47**

Yeah, well, there's a bunch of terms. So, like, you can be a hauler shipper. So, for example, if you're the shipper, you're the depot, and you have your own trucks, you can be a hauler shipper. If you're just a shipper and you're contracted out to drivers, then that would be the driver role.

**00:13:48 - 00:14:05**

Okay. All right. So this would be, in my terminology, or your terminology, the carrier. So my question then is, why would a carrier create transactions?

**00:14:09 - 00:14:11**

Because I think the transaction will be their pickup, right?

**00:14:16 - 00:14:17**

Okay.

**00:14:24 - 00:14:26**

But you give them the ability to delete.

**00:14:33 - 00:14:35**

To delete the transaction, yeah.

**00:14:39 - 00:14:41**

So you're saying that they can delete a transaction.

**00:14:50 - 00:15:00**

So they can access. They can read. They can update sites. They count. Yeah.

**00:15:03 - 00:15:14**

I think it probably makes sense now that you've got this. Roles and their capabilities is to do a quick workshop with Mohsen and Mark on this.

**00:15:16 - 00:16:21**

That's where I was leading to. Not that I got the extreme details. And trying to understand Mark and Mohsen's thought process against the security levels. And they probably can answer the questions better than you can. Why they would have all this access? If because they're just truck drivers, right? The truck goes, picks up the bags on mobile apps, says, Okay, I picked up the bag and I come back. Also the fact that the the truck I'm trying to think like, and I'm limited in my experience. And I sort of sent the question to Taz and Aaron. And I got back, I'm not understanding your question, so I got a meeting set up. But why would the truck need to know if they're taking a mega bag of PET 0 to 1 liters or a mega bag of aluminum?

**00:16:21 - 00:16:35**

Like, I'm trying to understand why they need this transactional data. So, yeah, so let's set up a security conversation just so I understand better, right? Yep.

**00:16:46 - 00:16:46**

Okay.

**00:16:46 - 00:16:47**

Okay.

**00:16:49 - 00:17:06**

All right. That's no longer found. That's no longer found. Oh, got another one open. And there it is there. Okay. So this is your training document, right?

**00:17:06 - 00:17:06**

Correct.

**00:17:10 - 00:17:11**

Okay.

**00:17:11 - 00:17:37**

How do you see the training? How did you organize the training? And we're just going to talk about the setup portion first, okay? Yep. How do you envision doing the training of setup? How do you want to run the class?

**00:17:38 - 00:18:18**

Yeah, so I think your intention, and correct me if I'm wrong, was for them to be hands-on, right? So they'll have to bring their computers and have their account and everything. And then the idea was to sort of walk them through the setup menu, and it's in the order that – so first of all, I would cover – I don't know if you scroll down a bit. So the reason I'm showing both is so that they're not confused while we're not tackling the top part of it. Because that's a different training session. So this is focused specifically on setup. And then I put in the note here about there is a specific order that's required, so that's all that first note is, is to say you have to do materials, shipping containers, and then products.

**00:18:18 - 00:19:04**

And then we actually start the training in the materials piece, so explaining basically what it is, how it's used, and then how to set it up. So this is the part where when we get the how to set it up, We will get them to navigate to the materials, so basically follow these instructions, access the materials module, and then they would enter the data. So this is where. And you and I talked about this as well as having some things they actually want them to create. So so where are the real materials? And giving them that list? So it should be chunked up by materials, it should be chunked up by the shipping containers, etc. So that when they get to that part, they refer to the document that maybe they have on their desk beside them of what you want them to enter.

**00:19:05 - 00:19:13**

So that'll be some real information. And they go in and they actually enter the data following the instruction and then click save.

**00:19:15 - 00:19:15**

Right.

**00:19:15 - 00:20:05**

Okay. So I have a favor to ask because you sent it to me as a PDF file. Yeah. Okay. Can you send this to me as a Word document? Because this is what I'm going to do. All right. So in the Word document, I'm going to basically delete all this type of stuff, okay? But when we get to the first material right here, how to set up materials, okay? I'm going to write, I'm going to copy this. Well, if it's a Word document, what I'll do is actually under here, where is it? Oh, yeah, here. Move this down. And say, okay, here's your data for materials.

**00:20:05 - 00:20:06**

That's a good idea, yeah.

**00:20:08 - 00:21:06**

And what I'm going to do is I'm going to separate out to each of the people and say, okay, Taz, you set up, I can't even think of a material item off the top of my head. You set up this material item. Aaron, you set up. So what I'm trying to do is create separate. Training packages for each member so that they have. This will be the official document that goes in support models, that goes into their doctor, their directories. But from a test case process, slash training process. As we hit each of these sections, we stop and then we get the individual to to enter the data based on the information I have. And it'll be separate. Like Aaron will have to enter something different than Taz, Andre, Sharif, okay?

**00:21:08 - 00:21:35**

So if you wouldn't mind just sending it to me in Word, then I can create that document rather than having to retype. And what was really annoying when I was trying to do it myself is trying to get a blank stuff in, you know, so many screen captures. And then when I saw this, I went, well, it's all here. All I need to do is, you know, okay, let's take a few seconds here and actually do it. And that's what I want you to do.

**00:21:35 - 00:21:38**

Yeah, that makes sense. That's a really good idea, Don.

**00:21:39 - 00:22:15**

Okay. So what I would expect, this is how I would expect the training would happen. You'd go, okay, team. This is how you would, you know, all the other gobbledygook. And now we're going to set up material. So this is how you do it, you navigate to materials you know you, and you're showing this, access materials, and this is how you add the new material. And you verbally tell them to do that, and then when you're done and you tell them about key consideration, then you go, Okay, go ahead. And each of you do the, uh, the test case called Setup materials, right?

**00:22:16 - 00:22:16**

Yep.

**00:22:16 - 00:22:20**

And that's when we'll actually stop and they'll set up the materials.

**00:22:20 - 00:22:23**

Yep. That's a really good plan. I like that.

**00:22:24 - 00:22:32**

Okay. And then when everybody's back, then we go, okay, now we're going to do shipping containers, right?

**00:22:33 - 00:23:15**

Yeah. So that makes a lot of sense because basically we're going to just. Be describing and talking about the theory. So what is it? How does it work? And so on. But it's the doing that they're going to learn from. And then they'll be able to use this document, which is why I did it this way, as kind of like, they're not going to remember everything. I mean, the rule is that the 100% that we deliver, they're probably, if they're lucky, going to remember like 60% of it. So they're going to want a document to be able to fall back on and go, okay, I need to go back and understand a little bit more. And that's why this guide is created the way it is, so that it's a takeaway also after the training that they can refer to.

**00:23:16 - 00:23:23**

Right. Then they can actually put this into their directories along with their individual test cases that they can refer back to.

**00:23:24 - 00:23:37**

Yep. Yep. Okay. I don't mind doing that. I'll send you the Word document. And, yeah, if you just want to insert the tables or whatever that says, Taz, you're doing this, and Aaron, you're doing that. Yeah.

**00:23:38 - 00:23:44**

That will work. Rather than me, you know, basically trying to copy and paste in a PDF doesn't always copy right.

**00:23:45 - 00:23:47**

No, it doesn't. No, I'll send that to you.

**00:23:48 - 00:23:49**

Perfect.

**00:23:49 - 00:23:50**

Yeah, I don't mind at all.

**00:23:53 - 00:23:53**

Okay.

**00:23:53 - 00:24:28**

But yeah, that's that's. The idea is to walk through each of these sections, describe what it is. So it's just because because they don't know that they haven't been in the product. And and the takeaway after this is like, you know, now that you've had the training, go in and play with it. Because because there's, there's so much in there, dab, like, there's, uh, there's those little um i, the letter I icons, that they're little pop-ups of additional information. So, I mean, this document would have been 2,000 pages long if I tried to include all of that. But they should go in and open those things up, right, just to see what they say and what they do.

**00:24:30 - 00:25:35**

Thank you. I knew I forgot to say something to you regarding the document. So I don't know if you want to make a separate document. Or add it to this one, okay? I was actually thinking it should be just under this section here, even before you get to the menu, is notes about this, that, you know, all these little exclamation marks, where the support module is. Because... In every conversation I've had with the team is, well, if I have a question, where do I go? If I have a question, where do I go? So it's almost in my head that we should, that's the first section we should talk about, give an overview that if you go up to this icon here, click on support, it brings up this page, right?

**00:25:36 - 00:25:49**

And I forget where the other eye is. This eye here is the information one, but where was the other? Nice little eye? Of course. Did I screen capture? Probably not.

**00:25:49 - 00:25:58**

Yeah, it's. There's a bunch of eyes throughout the I give. You go actually into sites so that you remember you sent me that screenshot of sites.

**00:25:58 - 00:26:01**

Oh right.

**00:26:01 - 00:26:06**

If you go in there, there's a couple eyes in there. Then if you expand it, it gives you a little bit more information, but.

**00:26:08 - 00:26:23**

So I couldn't figure out why I wasn't seeing my stuff, and I forgot that I was turning around. You're still in. That's where that back button would be really nice.

**00:26:23 - 00:26:26**

Yeah, wouldn't it? That's crazy talk.

**00:26:27 - 00:26:29**

Yeah. Yeah, here we go.

**00:26:33 - 00:26:46**

Yeah, so if you see, like, has itemized weight station, there's a little I at the end of it. Itemize It's, uh, the second box, oh.

**00:26:46 - 00:26:47**

Yeah, there it is, yeah.

**00:26:47 - 00:27:06**

So that's. Those are little pop-ups that give a little bit of additional information, so right? So if they want to know like, what, what is this? They could, you know, they should click on those, those kinds of things that that's where the going in. And familiarizing themselves with it and playing around with it and reading those little pop-ups is going to be helpful.

**00:27:06 - 00:28:03**

Yeah, so yeah, I've read those. That's what really started me on the support part of it, and even why I had to send you that because it might make more sense to them. But I didn't understand what this was saying to me and how it related to ABCRC. So that's why I sort of did a screen capture and asked you, what exactly is this? Oh, here's the other problem. See how this eye won't give me that information? Yep. But if I do this, oh, I've got to add it, sorry. All right. And that's critical. So if I'm on a site that's not in edit mode and it doesn't have a check mark, this eye doesn't pop up.

**00:28:03 - 00:28:03**

Yep.

**00:28:05 - 00:28:41**

And I didn't realize that until after I sent you. The email. Because I was look looking at it from this, this point of view, where here I am in the site and going, Oh, yeah, what is a receiver? Assignment is required. What is that, what is that? So then I went to support, trying to find the answer, because that's grayed out and the same with down here, right? This one actually works. So a couple of little bugs.

**00:28:41 - 00:28:43**

Yeah, it's because that one has a checkmark already.

**00:28:44 - 00:28:56**

Right. And I know I used the term bug, but for an end user, they'll be like, why is this information available, but this one's not? Yeah.

**00:28:57 - 00:29:00**

That's good feedback. I'll take that back to the team, actually.

**00:29:02 - 00:29:15**

Yeah. So in my head and my preference, anything that has an I.Whether there's a check mark or not, because it's a support item, it should be available.

**00:29:15 - 00:29:17**

Yeah, I think so, too.

**00:29:17 - 00:30:04**

Because dollars to donuts, everybody's going to forget. Well, why can't I see this? Why can't? And go, Oh right, because I did the exact same thing, right? Yeah, without going into edit, and then when I go to edit, it's available. So, yeah, anything for an information point should be available, whether there's a check marker there, because I could be working on it and go, do I need to do a receiver assignment for this site? You know, after I saved it and everything. And then going, what is receiver? Oh, okay. Right? Yeah. What I'm trying to do is stop the amount of times, as you see, how many times I have to go back and forth, back and forth, right? Yeah. If I have the answers.

**00:30:04 - 00:30:49**

And that's terrible during training when you start bouncing all over the place. It's really hard to follow. They're like, oh, my God, I'm so confused. That's why I try to organize the training like in a logical, like let's do it one step at a time. And rather than go, okay, well, let's set up products. And then, oh, by the way, we can't finish setting up products because we have to go in and now set up materials. And then you still can't set up your product because you haven't done your shipping container. It doesn't make any sense because then you're bouncing around and they're like, Oh my god, this is so hard to follow. So that's why I I went through it. I spent actually quite a bit of time going through, laying out the logical process and where the dependencies are, and tried to formulate the training that way.

**00:30:49 - 00:31:40**

Right? So I did like I did, like how you organized it very much, and yeah, I made. Right ordering that sort of to our discussion. This should be in the right order also But for the training purposes, yeah Doing it this way is perfect and that that way they're not bouncing around But as part of training to you go, Okay, and if you forget, like, especially in the site setup, if you forget what X is after, you save it. Because Here's the thing. When I'm creating a site, I can go in, do some of these fields, save it, come back later. But then I'm looking at it as if it's complete site, right? Yeah, yeah.

**00:31:40 - 00:32:21**

That's the other, um, I would say, less than an intuitive piece is that? Like, when you're in a menu like that and it's showing like the sites, so if you you go back and it shows that list of sites. There's nothing that really tells them by clicking on that, that it's going to open like additional details. So somebody could come to this screen and go, Okay, so good, there's Calgary plants, so what? But if you click on it, it actually expands it to give you more information, right? There's nothing that that really tells you that. And so that's something we need to emphasize. Is like, if you go to a page like this and then you want to drill down, just click on it.

**00:32:21 - 00:32:26**

Right. So here's the other question is, what's this box for?

**00:32:28 - 00:32:39**

So that's if you want to archive stuff. So if you wanted to bulk archive, you could select multiple and then click the archive button or whatever. Right.

**00:32:39 - 00:32:43**

But you and I know that.

**00:32:43 - 00:33:07**

Yeah. Otherwise, it doesn't do anything yet. And it's not. That's the thing is. And just so you're aware, from my perspective, I'm really pushing the product team to focus on. The customer experience side of things. So usability and things, they can put all the functionality in the world in, but if it doesn't make sense to the user, then we're missing the mark. Right. And so here's the.

**00:33:07 - 00:34:06**

Here's the thing. The word archive is way up here and I understand what this is for, but we have all this text here. So what's this box for? And somebody may go, well, okay. And, you know, try to do stuff, right? So, Yeah, somehow this is going to be – because when we design and implement software, we have to make it to a five-year-old mentality, right? Yeah. Very simplistic, very informative. Because you're going to get that end user and, you know, if you think that they're smart enough and you gave them a min level and they went in here, oh, that's what I wanted to ask. And I was a little bit afraid to do it, okay? So this particular site, right? Hopefully, and I want to archive it, all right?

**00:34:07 - 00:34:20**

So I hope I don't screw myself up. So then I click archive. It says, are you sure you want to archive this site? If I say yes, it disappears, correct?

**00:34:21 - 00:34:21**

Correct.

**00:34:30 - 00:34:36**

And then my question is, if I realize I accidentally archived the wrong site, how can I bring it back?

**00:34:41 - 00:34:43**

Good question. Not sure.

**00:34:44 - 00:35:18**

And that's a big mistake that I can see happening is they're selecting, oh, I want this one. I want to view all these three, right, because I'm selecting them. And then go click up here to archive and end up. Archiving all these, how can I bring it back? Is that a ticket to you guys? Uh, is men have the ability to bring it back? Um, even though there's a warning there, that mistake will happen.

**00:35:18 - 00:35:21**

Yeah, I think even that warning could be updated.

**00:35:21 - 00:35:22**

Right?

**00:35:22 - 00:35:25**

It could say, like, if you archive this, you can't retrieve it, right.

**00:35:25 - 00:35:44**

Right? If that's the case. Or if you need to retrieve it, you must submit a support ticket with the information. But then if the information is gone, it makes it more difficult, right? So, yeah.

**00:35:46 - 00:35:59**

Something is telling me that from one of our other customers, if it's archived, you can't bring it back. You have to create it new again. I'll confirm.

**00:36:00 - 00:36:00**

Though.

**00:36:01 - 00:36:06**

Dad. Don't take that as gospel. I'm trying to recall if that's the case.

**00:36:07 - 00:36:36**

Yeah. So my question to that, though, is if I have to create new. So let's say that that's how it's done, right? If I archive it, I have to create new. Well, when I archive that site, what does it do to all the history of that site? Does all the history disappear? And if so, when I create a new site, how do I get that history back to that site?

**00:36:38 - 00:36:53**

Yeah, I think it preserves the history, but I'm not sure if you create a new that you would get the history back to the new one. Basically, it treats it as a new site. The other gotcha, I think, is that you can't reuse the email.

**00:36:59 - 00:37:01**

I think we have to revisit that particular.

**00:37:02 - 00:37:11**

Yeah, let me dig into that a bit and come back with a real answer for you. I'm making some assumptions that I'm not entirely clear on.

**00:37:12 - 00:37:33**

Yeah. Yeah, we've got to revisit that. And if the end result is a support ticket has to be generated, well, that's what it is, right? So we have to make sure people are really careful. I can just see mistakes happening, and then they're scrambling to get the stuff back.

**00:37:33 - 00:37:47**

Yeah, because I think it may be retrievable, but it would be on the database, at the database layer, so it would have to go to our dev team to recover it probably. I'm not entirely sure, but I will find out for you.

**00:38:02 - 00:38:43**

And hopefully you have the answer before we go into training because when we go to sites, we're going to have to talk about archiving, right? And we have to impress upon them. It depends on what you find out, the end result of archiving a site. So I'm going to take this off so I don't do it. I was actually very nervous about trying it myself going, and I don't have the information. And I was thinking, well, I can do all these screenshots, but then what happens to my transaction? There was too many questions for me to try and do an experiment. Okay. So, yeah. So we really got to point that out in training.

**00:38:48 - 00:38:51**

Talked about the help desk. So I'm just going to close that so I have access to there.

**00:39:16 - 00:39:16**

Incentives?

**00:39:16 - 00:39:28**

This has caused a lot of conversation on our end, so we're still in discussions about it. They're trying to get their heads wrapped around it and whatnot, which is fine.

**00:39:28 - 00:39:40**

Yeah, I think the so, the information I sent you, I hope that was helpful. It's a little more, there's a bit more information in there than than what's in this document, but.

**00:39:43 - 00:39:45**

Yeah, and I shared it with the team, so that's good.

**00:39:49 - 00:39:56**

I tried to include some examples and stuff to help you wrap your head around what it is, how it's used.

**00:39:58 - 00:41:29**

All right. Okay. Also as part of the training, I made the mistake and cleaned my office on Sunday. And I can't find my page of questions and discussion points for this meeting. I looked for it all day yesterday and I'm like, where did I? So I think I accidentally threw it out. Whoops. I'm open to whatever you think. When I bring this next point to you. So this training is simply the setup section. Correct. Okay. And I'm thinking out loud here. How do we impress upon the team for the first training session that that's all that we're doing in this training session? Do you think it's okay verbally? The reason why I'm asking this is when I first looked at the document, I thought this document included the upper menu too.

**00:41:36 - 00:42:00**

Yeah, so that's part of the reason why I put this in here was to say, you know, there's two parts to the menu, and the part we're going to be focusing on today is the lower part of the setup. Then we can say, you know, your day-to-day activities, there will be another session for that, and that's going to be like Mohsen and I are going to have to tag team that because he understands how your team is going to use the product better than I do.

**00:42:02 - 00:42:17**

Right. I'm just wondering. I guess verbally we can just really nail it home to the team that it's just the bottom section that we're talking about in this meeting today.

**00:42:18 - 00:42:33**

Yeah, I mean, they can't do anything else until setup is done. Yeah. You can't do transaction or claims or, you know, set up sites or any of those things really until you've done the setup.

**00:42:41 - 00:43:30**

What about this idea? Just like a red box around this. And in the setup note here, another sentence along the lines of setup must be completed first before you can do any day-to-day activities. Yep, you can do that. Just flag it a little bit more because I'm also thinking that. You know, after these guys are trained, they're going to have to train their own people and they're going to use this document. And the fact that we'll have another document for the top part that just flags that this document is regarding setup and setup only.

**00:43:30 - 00:43:35**

Yep, this is the configuration piece of it, yeah.

**00:43:38 - 00:43:48**

Just so it's really pulled out for them to know that, okay, in this document, they're not doing anything. They did it today stuff. It's just set up.

**00:43:51 - 00:43:53**

Yeah, I can put a red box around it.

**00:43:54 - 00:43:55**

Perfect.

**00:43:55 - 00:43:57**

Add some additional detail, no problem.

**00:44:04 - 00:44:16**

And I did like this when I saw this. Second paragraph was perfect. I thought, yep, yeah.

**00:44:16 - 00:44:29**

I think it's important to emphasize that piece. So they know why we're not starting with, uh, with products, like when they look at the menu, it says products. We're not starting like we're jumping halfway down. Right, right.

**00:44:29 - 00:44:34**

Because I ran into that same problem when I was playing with, I kept going to products first, right, yeah.

**00:44:34 - 00:44:49**

Yeah, you would, right? That's that's why, that's why I pushed on the the product team to say like, this is to me. It's not logically organized, like if there's dependencies, then you should have those things together, grouped together, right?

**00:44:49 - 00:44:59**

So, yeah.

**00:44:59 - 00:45:10**

That's the plan to have is to walk them through this document and actually have them do it. So we'll go section by section, explain what it is, what it's for, how it's used, and then have them set it up.

**00:45:14 - 00:46:18**

So like I said, you're going to send this to me in Word, and then I'm going to break out so I have multiple copies, one for Aaron, Taz, Sharif, and Andre. And each of them will have – I need you to put this shipping container in, Andre, and whatnot. And that's what they'll be bringing to the training session on that day. I'm also going to – so I booked a room at ABCRC and going to have the team actually come into that room, the boardroom, right, the big boardroom. And I'll have you up on screen so that they can see everything you're doing, right, on the Teams call. And I think what I'll do is I'll get permission from Shane to bring Andre down for that training session, maybe like a half day down here in Calgary,

**00:46:18 - 00:46:47**

so that they're in the room so that I can help out, rather than them in their individual offices. Trying to do it because I just have a funny feeling that if they're in their office, they're going to have people knocking on the door, interrupting them. And whatnot. And so the other thing is, David is not part of these training sessions. Right.

**00:46:47 - 00:47:02**

So is your intention to have to share the like if we record it, which I assume we will, is to share the recording with David afterwards so he can. So he can see the product? Because I think that's been one of his complaints is he doesn't know the product, right?

**00:47:02 - 00:48:08**

Yeah. So the decision with Sam, Shane, and I is that regarding David and Prithi, who's our security guy, I'm going to be doing individual training with both of them outside the operations team. Because David wants to know things technically. And I need the operations team to use this application as operations and not get confused or derailed because of the technical questions David will ask. Okay. So am I one to ones with the security team and David? If they hit me with a question, I'll just record that question and fire that off to you. Yeah, I don't want to. We've had too many meetings in which David was part of where we're trying to get information from operations or educate operations.

**00:48:08 - 00:49:09**

And we went down too many rabbit holes in the technical realm because the other thing I'm trying to do, and this was the conversation I had with Sam and Shane, is David can't support this application. He can't, he can't do anything to this application, he can't correct fields, he can't. Nothing like this is your application. Duane, Not his. You guys manage it, you guys take care of it. He's responsible for the NAV side, and so, yeah, just a data overview with him is all that's going to happen. He's. I'm trying to break his mindset that if there's a technical issue that he's to resolve it. And no, it's diverse's responsibility to resolve it. And sort of that's why I keep talking to you about the support stuff, right?

**00:49:10 - 00:49:33**

The more that I can push the team to these support modules or these information modules, right? Because they don't have that nav now. So the more I can get them thinking about this, the better chance I have at the operations team not automatically reaching out to David.

**00:49:37 - 00:49:38**

Yeah, makes sense.

**00:49:40 - 00:49:50**

He's really great at nav and everything. But, you know, after 500 years, it's like, no, David, this does not fall on your shoulders, buddy. Yeah.

**00:49:51 - 00:49:57**

Yeah, maybe that's part of his apprehension. He thinks he's going to have to support all of this, and he just doesn't know.

**00:49:58 - 00:51:20**

Yeah. Yeah. And it's going to take a bit for us, not just with me, but Sam and Shane, repeating to him, you don't support this application. If there's something broken in it, Diverse supports it, not you. That's true. If there's a mistake made, diverse will support in resolving the mistake, whatever it is, not you. If there's some type of adjustment that has to be made on the transactions or actually the QC side. Oh, that's right too. If there's a mistake here, it's got a technical mistake, it's got to be fixed by diverse. My question to you, so who am I? Okay, so I'm at my normal level. And so I've made some changes in what originally was set up here, just because these are the right numbers. But this is what threw me was that this, Line here this quality control.

**00:51:20 - 00:51:42**

So they're going to scan the tag, right? Yep, and then that will populate other fields within here, right?

**00:51:42 - 00:52:00**

Yeah, so they're going to search or like this. This field is basically to search for something that's already been entered. So once they've already done, once there's audits in the pipeline, they can go in and search for specific things in this screen.

**00:52:03 - 00:52:45**

Okay, so if a peg, so we've scanned these and we have to send a bunch of these to QC, right? So they're now in the QC pipeline. And I'm the operator at the QC. I guess I'm a little bit confused. So I have something in QC. So this is...

**00:52:51 - 00:52:54**

That's probably the one that Mohsen put in there during the training.

**00:52:55 - 00:53:21**

Yeah, and I keep going back to it. That's another record. Okay, the feedback I have is this QC section, and I've gone back to the video, is not sitting in my head. To how it works.

**00:53:32 - 00:54:17**

I think maybe I think part of it is that jumping around. So like whenever they're delivering stuff, you remember where he was like, well, I don't think I really have that quite set up correctly. And then he's got to jump and configure something and then come back and look to see if it's there and all that. That jumping around gets people confused. So I think it's going to be on us, on me, and by us I mean diverses, to put together similar to what we're doing with the setup training is how these things actually work. What are the dependencies that need to be put in place? So, yeah, that's my next task, basically, is to go through that top part of the menu.

**00:54:18 - 00:54:36**

And build out a similar document to what I've just done for setup that shows the screenshots, does an explanation of how these things work, what the dependencies are, and so on. So a better explanation. It will be basically founded on the information Mohsen provided, but in a much more organized way.

**00:54:38 - 00:55:07**

So do you think we should actually have a separate QC training session? Because that's what I'm leaning towards. We'll actually force bags into QC and they'll have to go out onto the floor and key in data and everything into the system. And so it's reflected back.

**00:55:09 - 00:56:05**

Yeah, it probably makes sense because the QC is a bit of a beast. Like there's quite a lot to it, right? And it's the most complex part of the software right now, so probably doing that separate is a good idea. I know we also talked about the shipping container management piece, or sorry, the inventory piece, that you didn't want to do that until CBIL. So we'll have that as a separate section as well? Yes. Yes. So I still need to go through that top-level menu. And understand what's actually applicable to you and and then, um, and then organize the training that way. So, yes, we we can probably do the, uh, the shipping container or the supply inventory by itself. We'll do a specific training section for that, and then one for, uh. Quality control Okay.

**00:56:05 - 00:56:11**

I like that idea, because, yeah, I'm struggling with quality control. I haven't touched the inventory module yet.

**00:56:11 - 00:56:37**

You're not the only one, by the way. I mean, it's new to most of us. So the people that have been working on it, which is product and development, they understand how it works. The rest of us, we're just starting to see it now, just like you are. So, yeah, even my support agent that's been here two years now is finding a lot of the new functionality complex. So you're in good company.

**00:56:40 - 00:56:41**

Excellent.

**00:56:43 - 00:56:43**

Okay.

**00:56:43 - 00:57:07**

I'm trying to put a lot of rails around some of this stuff and a lot of clarity around it. By providing examples and all of the detailed documentation. That's organized and has a nice flow to it and talks about dependencies and things like that. Even the products piece, there's nothing stopping you from going in and creating a product. You just won't be able to finish it.

**00:57:08 - 00:57:09**

Right.

**00:57:09 - 00:57:16**

Right. So what's the point in doing it? If you don't have all of the other pieces in place, then, you know, what's the point?

**00:57:20 - 00:57:26**

Exactly. Okay, so we're agreed that we're going to do supply inventory module and quality control in separate training classes.

**00:57:26 - 00:57:44**

Yeah, so the note I took from the conversation with Mohsen was that you want to do the supply inventory piece after CBIL is ready? Yes. So that's one note. I know there's going to be an April release, Dev. I'm not sure if you were made aware.

**00:57:45 - 00:57:46**

Oh, no, I wasn't.

**00:57:47 - 00:58:22**

Yeah, so they're going to do an interim release in April to try and get some more of the functionality in the product faster. So it's new as of, I guess, late last week that they made the decision. So I'm not entirely sure what's going to be in there yet. So give me some time to figure that out. Yeah, we might have some of the additional functionality that Mark had talked about. Remember he did the presentation when we were on site about what's in three and what's in four? So what's in four, some of that might be available in April.

**00:58:23 - 00:58:38**

Okay. I'm going to put a condition on the release date, though. It has to be after. Days after April the 5th.

**00:58:38 - 00:58:42**

Yeah, I don't think it's going to be until the end of April.

**00:58:43 - 00:58:48**

Okay. So why am I saying after April the 5th?

**00:58:51 - 00:58:56**

Oh, you've got visit Easter weekend?

**00:58:56 - 00:58:58**

Yeah, that's Easter, yeah.

**00:59:00 - 00:59:01**

Yeah.

**00:59:02 - 00:59:07**

Yeah, I don't want them to release something and it blows up and everybody's scrambling to their ease to break.

**00:59:08 - 00:59:20**

I know from talking with Dayhan that they've just basically put it into some of the functionality that's going to be released in April. They put it into QC.

**00:59:21 - 00:59:22**

Oh, okay.

**00:59:24 - 00:59:26**

Yeah, so it won't be until end of April.

**00:59:27 - 00:59:38**

Perfect. I just don't want your team to have. Do a release and they lose their Easter weekend, especially with Molson. This is his child's first Easter.

**00:59:38 - 00:59:52**

Yeah, agreed. Yeah, so there's going to be an interim release, so that's good because some of the functionality that didn't make it into the release three will be here sooner than we thought, so that's good.

**00:59:53 - 00:59:54**

Yeah, definitely.

**00:59:56 - 00:59:58**

I just don't know what that is yet.

**00:59:59 - 01:00:03**

And that's fine. That's perfectly fine.

**01:00:04 - 01:00:07**

I'll let you know as soon as I know what's in there.

**01:00:08 - 01:00:30**

Yeah. Yeah, so I'm just actually thinking here. I think I'd actually have to put a condition on the release date that it has to be after our two training sessions, right? Because I don't want a whole menu change or something happening while we're trying to train them, right?

**01:00:30 - 01:00:31**

Yeah.

**01:00:34 - 01:00:46**

I mean, it'd be more of an impact to you in the training. But yeah, if all of a sudden we got new menu items or something while we're trying to train them.

**01:00:47 - 01:01:11**

Yeah. I think we're still good with the dates that we have. Yeah, but let me dig into what's actually being released and then I'll be able to assess impacts. And and then, if if we need to, then push it out beyond the release. Just to be safe. But I don't think we're going to have to, I think we're, I think we're going to be good, right?

**01:01:11 - 01:01:19**

And you're going to create the second instance of the UAT environment that we're going to use for training, correct?

**01:01:19 - 01:01:32**

Uh, you should already have it. So it's called ABCRC underscore ops underscore train, and I sent you an invite to the account.

**01:01:34 - 01:01:39**

All right, just one second. It might have got hit by our security thing.

**01:01:41 - 01:01:50**

I believe that I sent that Thursday or Friday. If you need to resend it, I can. It's no problem.

**01:01:51 - 01:01:52**

No, just...

**01:02:33 - 01:02:37**

I can't find anything that says a new site.

**01:02:47 - 01:02:51**

I just reset the invite. Okay.

**01:03:06 - 01:03:30**

Just waiting for it to come in. Did you feed your hamsters this morning?

**01:03:35 - 01:03:42**

I got the email right now. It's d-s-i-c-i-l-i-a-n-o at abcrc.com, right?

**01:03:44 - 01:05:05**

Yeah. Oh, there. It just came in. Okay. Click this link. This is training. And that was from the link you sent me. I think that's why I'm a little bit confused. All right. Okay. So this is the email you're talking about, right?

**01:05:10 - 01:05:10**

Yep.

**01:05:10 - 01:05:19**

Please click this link to complete your setup. So it takes me to training.diverse.

**01:05:34 - 01:05:38**

You can see in the top menu where it says ABCRC ops underscore training.

**01:05:39 - 01:05:40**

Yeah.

**01:05:40 - 01:05:44**

See, that's equals ABCRC. That's the right one.

**01:05:51 - 01:05:53**

That's weird. Okay.

**01:05:53 - 01:06:08**

So I have the password. He said password token not found. What's the URL to log in?

**01:06:16 - 01:06:21**

Because that's just creating a password to complete your setup.

**01:06:25 - 01:06:29**

I bet you it was pulled in by security there. Okay.

**01:06:32 - 01:06:45**

Do you have the link to... where it is? Let's try getting out of all that.

**01:06:45 - 01:07:08**

I wonder if it's because it's using the same password or the same email. Yeah, this is yours, that's the create password. Yeah, yeah.

**01:07:08 - 01:07:12**

So I created the password. But now it says the password to create it.

**01:07:21 - 01:07:22**

That's the right one.

**01:07:23 - 01:07:24**

ABCRC ops training.

**01:07:32 - 01:07:38**

Oh, hold on. That's locked me into there. So let me try getting rid of that. I'm looking for the primary URL.

**01:07:39 - 01:07:40**

That should be it.

**01:07:42 - 01:07:54**

Okay. That's office training up there. Oh, no, it's bringing me back to the main one.

**01:07:58 - 01:08:00**

So if you log in there, what do you get?

**01:08:02 - 01:08:03**

Oh, I get the same account.

**01:08:04 - 01:08:06**

You just get the ABCRC train one?

**01:08:07 - 01:08:09**

Oh, hey, hold on.

**01:08:09 - 01:08:11**

There you go, Oh.

**01:08:11 - 01:08:22**

This is new, okay, so it took a few seconds, I guess, to to come through. There you go. Okay. So the URL is the same.

**01:08:22 - 01:08:36**

Yeah, you'll see at the top where it says, ABCRC ops training. Um, right underneath your name there in the top right corner here, so you're in the right. Yeah, yep, that's the one, okay.

**01:08:36 - 01:08:36**

So.

**01:08:37 - 01:08:38**

Brand spanking new and clean.

**01:08:43 - 01:08:45**

So this must be the old one, right?

**01:08:45 - 01:08:46**

Yep, that's your original.

**01:08:48 - 01:08:48**

Nice.

**01:08:48 - 01:09:09**

So that's the one we're calling yours now, Dev, and that's the one you can give Joe access to to do the API stuff. And the other one is for the ops team to go around and play around with and do the setups and stuff. So in the ops, when you'll need to create their accounts and things like that, for them so they can log in when we're ready.

**01:09:11 - 01:09:11**

Yeah.

**01:09:13 - 01:09:16**

Yeah. So this is the one I'm going to create their accounts in.

**01:09:16 - 01:09:17**

Yeah.

**01:09:17 - 01:09:31**

Okay. So I can't rely on that. I got to rely on that. But okay. So the login screen, so the new login screen where I can select which environment I want to go into. Yeah, that's brilliant. That's perfect.

**01:09:34 - 01:09:44**

Yeah. I had that. Done on the 20th, so a few days ago. I think the Friday, I think they sent it to you. But anyway, regardless, it doesn't matter. It's there now.

**01:09:45 - 01:10:01**

Yeah, I'm just looking at the actual email. It might have got pulled because it's an invitation via US East to Amazon's. So it might have got pulled by our filter system.

**01:10:01 - 01:10:10**

Yeah, it could be. That's fine. I'm glad we talked about it. Otherwise, you'd still be wondering why that hasn't been taken care of. Yeah.

**01:10:12 - 01:10:34**

It was one of the questions I needed to ask you when it would be done. So it's done. Yay. And it's nice and clean. You seeing what I'm seeing?

**01:10:39 - 01:10:39**

Settings.

**01:10:39 - 01:10:44**

In setup here? Yeah. No API.

**01:10:45 - 01:10:48**

Oh, right. Probably hasn't been enabled.

**01:10:49 - 01:10:49**

Okay.

**01:10:50 - 01:10:54**

That might actually be okay for the ops one because we don't want to cover API anyway, right?

**01:10:56 - 01:11:28**

Right. Yeah. So, yeah. So the API ability after. The operations training and everything is done. Oh, here's a question you can take back. It's a secret key in this environment, right? Does it automatically translate to this environment?

**01:11:33 - 01:11:39**

Sorry. If you set it up in the operator account versus the participant account?

**01:11:40 - 01:11:52**

No, no. So if I set up a secret key in DAV's environment of diverse, does it automatically translate into the operations team?

**01:11:52 - 01:11:55**

No, no. They're two separate instances.

**01:11:56 - 01:12:15**

Okay. So then, yeah, I will need access to the API here after. So we'll say May the 1st to create the API keys that I'll have to then give to Joe of ABDA as we start ramping up more API connections.

**01:12:16 - 01:12:26**

But he could use your ABCRC account, like your ABCRC train. He could use the one that you're using, the one we're calling yours. He could use that environment.

**01:12:27 - 01:12:43**

Oh, yeah, that's the one we're going to work in. And once we have a proof that it's working, everything's good, then I need to switch over to the operations environment so that the transactions start coming through.

**01:12:43 - 01:12:48**

Yeah, true. Yeah, you just need to give them the new API.

**01:12:49 - 01:12:50**

Okay.

**01:12:51 - 01:13:00**

Uh-oh. Uh-oh. See what I'm in? ABCRC ops training.

**01:13:00 - 01:13:08**

Yep. It might be because it's cached. Should be clean.

**01:13:21 - 01:13:28**

Oh, they're linked. I logged out of the other environment.

**01:13:32 - 01:13:35**

I'm looking at it right now and it's got no sites.

**01:13:37 - 01:13:43**

Okay. So when I log into the other site.

**01:13:43 - 01:13:44**

It cached.

**01:13:45 - 01:14:41**

Yeah. So it pulls it from the same. So I need to. I got to be careful. I have to be careful. Other people and going, Okay, so Taz this, I have to make sure I'm in here and I've logged out of my other site. This one, um, but when I'm, uh, yeah, okay, so it's just on my end. I got to be careful, which is fair, which is fair. Okay, no, that's good. Because I thought I didn't see anything and then all of a sudden everything appeared, but that's because I logged in to the other site. So, yeah, so browsers. So it's in the browser base. Okay, no, that's good to know.

**01:14:41 - 01:14:54**

Yeah, there's still some setup that needs to happen for this account, just so you're aware. So, like, if you go into participants, participant profiles. Basically it says you can't do anything right now.

**01:14:55 - 01:14:56**

Oh, okay.

**01:14:56 - 01:15:18**

Go down just below products. Yeah, so this is where I have to go into the admin piece on our side and set up your participant profiles. So similar to what you have for your current account. So that's not done yet. But, yeah, that's on my to-do list.

**01:15:19 - 01:15:29**

Yeah, no worries. I'm staying out of this until after our training sessions.

**01:15:30 - 01:15:38**

Yeah, because I have to have it set up from that perspective. Otherwise, your team won't be able to do anything when they get to participant profiles. They won't be able to create them.

**01:15:40 - 01:15:45**

All right, because I've got to come in here. This is where I've got to create the participants, not my other account.

**01:15:45 - 01:15:59**

Yeah, you're right. So, for example, the participant types haven't been defined yet, so like the collector, hauler, processor kind of stuff. Right. Transaction type, same thing. So I have to go in and do all that, so I'll take care of that.

**01:16:00 - 01:16:04**

Okay. Then I'll set up the team.

**01:16:05 - 01:16:15**

Yeah, I'm just basically going to set it up the same way your ABCRC is. Like you're going to have your depots, and that's all going to be the same, so I'll set it all up the same.

**01:16:22 - 01:16:23**

Perfect.

**01:16:23 - 01:16:38**

All right, sir, that's all I had. So, yeah, I think we have our meeting tomorrow, so we'll cover it. I sent you some information on the decisions and the risk items, so similar to what we did with the action items, we'll put those into Monday and track them.

**01:16:39 - 01:16:43**

Right, right. So I figured that would be in tomorrow's discussion, yes.

**01:16:43 - 01:17:17**

Yep, that's all good. So, yeah, that's all I had. So if you're good to plan, I will send you the Word document for the training to put those additional pieces in. And just like you said, I think probably we'll do a bit of housekeeping at the very beginning and talk about the support, the support site that's available. And once they're logged in, they'll have the ability to go look at the FAQs and things like that. And then all of those little eye icons that have pop-ups. So that they know the resources that are available, and then we'll move on with the training from there.

**01:17:19 - 01:17:19**

Perfect.

**01:17:22 - 01:17:23**

That sounds great, sir.

**01:17:23 - 01:17:30**

All right. I think we have a plan. I love it when a plan comes together. Remember that, the A-team?

**01:17:31 - 01:17:32**

Exactly, yes.

**01:17:35 - 01:17:39**

What was his name? Hannibal? No. Was it Hannibal?

**01:17:40 - 01:17:43**

I'm trying to think. I remember Mr.T.

**01:17:43 - 01:17:54**

Mr.T. I think his name is Hannibal. Anyway. All right. Anything else from your side, Dov?

**01:17:56 - 01:17:56**

Nope.

**01:17:57 - 01:17:57**

Nope.

**01:17:57 - 01:17:58**

We're good.

**01:17:58 - 01:18:03**

Okay. Wonderful. I will give you 10 minutes of your day back.

**01:18:04 - 01:18:05**

Yay.

**01:18:05 - 01:18:07**

Thanks, bud. All right. Cheers.

**01:18:08 - 01:18:10**

Cheers. Bye. Bye.
