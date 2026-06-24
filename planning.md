Project 3: TakeMeter – Planning Document
1. What my TakeMeter measures
My TakeMeter looks at comments from the LeBron vs. Jordan debate and tries to figure out which side the person is on. So basically it reads a comment and decides if the person thinks LeBron is the GOAT, if they think Jordan is the GOAT, or if they didn’t really pick a side. I thought this would be cool because people say a lot of different things to make their point and I wanted to see if a model could pick up on that.
2. Labels I will use
•	pro_lebron – the comment is saying LeBron is better or the GOAT
•	pro_jordan – the comment is saying Jordan is better or the GOAT
•	neutral – the comment doesn’t really take a side or just talks about both players
3. Why I chose this topic
I picked this topic because the LeBron vs. Jordan debate is honestly one of the most argued things on the internet, especially on Reddit, YouTube, and Instagram. People get really passionate about it and use all kinds of different arguments like stats, rings, era, and character. I thought it would be interesting to see if AI could actually tell which side someone is on just from how they write. It’s also just a fun topic that I actually care about so it made the project more enjoyable to work on.
4. What my dataset will look like
•	Number of examples: around 20–30 (the minimum the project needs)
•	Format: each row has a text column (the comment) and a label column (pro_lebron, pro_jordan, or neutral)
•	Source: I collected real comments from Reddit, YouTube, TikTok, and Instagram by copy-pasting them manually
•	Cleaning: I removed usernames, took out most emojis, and tried to make the formatting consistent
5. Success criteria
I’ll know my model is working if:
•	It gets at least 70% accuracy on the test set
•	The confusion matrix shows it’s not just guessing one label every time
•	When I test it on new comments it hasn’t seen, the predictions make sense
•	It can correctly label obvious comments like “6-0 end of discussion” as pro_jordan
6. Risks / challenges
•	Small dataset: 20–30 examples is not a lot and the model might not learn enough from it
•	Ambiguous comments: some comments are hard to label even for a human, like when someone says both players are great
•	Sarcasm: some comments are sarcastic and a model probably won’t catch that
•	Class imbalance: I noticed most of my comments ended up being pro_jordan which could make the model biased
•	Slang and nicknames: people use names like LeFlop or LeFraud and the model might not know what those mean
7. What I expect the model to learn
I think the model will start picking up on certain words and phrases that show up a lot in each label. For example:
•	pro_jordan comments usually mention things like “6-0,” “rings,” “killer instinct,” “never lost in the Finals,” or “flopping”
•	pro_lebron comments tend to talk about “longevity,” “stats,” “versatile,” “illegal defense,” or ”era”
•	neutral comments usually say stuff like “both are great” or “it depends on what you value”
I also think the tone matters a lot. Pro_jordan comments tend to be pretty short and confident while pro_lebron comments often go into more detail trying to explain their argument.
