# Sentiments
This is a demo work for sperimenting sentiment analysis with python. There are three different types of demo work.
1. smile
2. tweets
3. pie chart web app

## smile app categorizes a word as positive or negative

```
$ ./smile love
:)
$ ./smile hate
:(
$ ./smile Standford
:|

```

## tweets app  categorizes a user's tweets as positive or negative

```
$ ./tweets @cs50
0 hello, @cs50
1 I love you, @cs50 
-1 I hate you, @cs50
```

## A website that generates a pie chart categorizing a users' tweets

![image of pie chart](https://user-images.githubusercontent.com/179784/30598798-6cd0a24a-9d63-11e7-8932-1cf2fb8428c5.png)


### Getting Started
- In a terminal window execute

```
    cd ~/sentiments/
    pip3 install --user -r requirements.txt
```
to install these programs' dependencies.

- Sign up for Twitter at twitter.com/signup if you don’t already have an account.
- Visit apps.twitter.com, logging in if prompted, and click **Create New App**.
  - Any (available) **Name** suffices.
  - Any (sufficiently long) **Description** suffices.
  - For **Website** any **URL**).
  - Leave **Callback URL** blank.
- Click **Create your Twitter application**. You should see "Your application has been created."
- Click **Keys and Access Tokens**.
- Click **modify app permissions**.
- Select **Read only**, then click **Update Settings**.
- Click **Keys and Access Tokens** again.
- Highlight and copy the value to the right of **Consumer Key (API Key)**.
- In a terminal window, execute
```
    export API_KEY=value
```
where value is that (pasted) value, without any space immediately before or after the =.
- Highlight and copy the value to the right of **Consumer Secret (API Secret)**.
- In a terminal window, execute
```
    export API_SECRET=value
```
where value is that (pasted) value, without any space immediately before or after the =.
If you close that terminal window and/or open another, you’ll need to repeat those last five steps.
Next, try running
```
./smile
```
to see how it works. Keep in mind that all words will be classified (for now!) as neutral because of that hardcoded 0 in analyze.py.
Next, try running
```
flask run
```

