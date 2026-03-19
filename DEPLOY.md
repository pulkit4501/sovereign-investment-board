# How to Deploy to GitHub

You have completely sanitized your code and removed any private Telegram tokens or API keys! You are now safe to publish this repository to GitHub.

Follow these steps in your terminal to create and push your local repository:

### Step 1: Initialize Git
If you haven't already initialized git in this directory, do it now:
```bash
cd /Users/pulkit4501/Desktop/Personal/Projects/finance_test
git init
```

### Step 2: Add and Commit Your Files
Add all the sanitized files to staging and commit them:
```bash
git add .
git commit -m "Initial commit for Sovereign Investment Board"
```

### Step 3: Create a Repository on GitHub
1. Go to [GitHub.com](https://github.com/) and log in.
2. Click the `+` icon in the top right corner and select **New repository**.
3. Name your repository (e.g., `sovereign-investment-board`).
4. Keep it **Public** (or Private if you prefer).
5. Do **NOT** initialize it with a README, .gitignore, or license, since you already have these in your local project. 
6. Click **Create repository**.

### Step 4: Link Local Repo to GitHub and Push
On the next page, GitHub will show you some code snippets. Copy the one under **"…or push an existing repository from the command line"**. It will look something like this:

```bash
git remote add origin https://github.com/your-username/sovereign-investment-board.git
git branch -M main
git push -u origin main
```
*(Run those commands one by one in your terminal)*
