# Data@UCI GitHub Workshop Part 2

Welcome to the GitHub Workshop Part 2! This hands-on tutorial will teach you the fundamentals of collaborating on GitHub through forking, committing, and creating pull requests.

## What You'll Learn

- How to **fork** a repository
- How to **clone** your forked repository
- How to make **commits** and push changes
- How to create a **Pull Request (PR)**
- Best practices for collaboration

---

## Getting Started

### Prerequisites

Before you begin, make sure you have:
- A [GitHub account](https://github.com/join)
- [Git](https://git-scm.com/downloads) installed on your computer
- A text editor (VS Code, Sublime Text, etc.)

### Verify Git Installation

Open your terminal and run:
```bash
git --version
```

If you see a version number, you're good to go! 

---

## Workshop Steps

### Step 1: Fork This Repository

1. Click the **Fork** button at the top-right of this page
2. This creates a copy of the repository under your GitHub account
3. You now have your own version to work with!

**Why fork?** Forking allows you to freely experiment with changes without affecting the original project.

---

### Step 2: Clone Your Fork

1. On **your forked repository**, click the green **Code** button
2. Copy the URL (HTTPS recommended for beginners)
3. Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/Data-UCIGithubWorkshop.git
cd Data-UCIGithubWorkshop
```

Replace `YOUR-USERNAME` with your actual GitHub username.

**What just happened?** You downloaded a copy of the repository to your local machine.

---

### Step 3: Create a New Branch

It's best practice to create a new branch for your changes:

```bash
git checkout -b add-my-name
```

**Why branches?** Branches allow you to work on new features without affecting the main codebase.

---

### Step 4: Make Your Changes

Let's practice making changes! You can either:

**Option 1: Edit the README**
Add your name to the "Workshop Participants" section below.

**Option 2: Create Your Own File**
Create a file called `YOUR-NAME.txt` with some information about yourself:

```
Name: Your Name
Major: Your Major
Year: Your Year
Favorite Language: Your Answer
```

**Example file (`jane-doe.txt`):**
```
Name: Jane Doe
Major: Computer Science
Year: Junior
Favorite Language: Python
```

---

### Step 5: Stage and Commit Your Changes

Now let's save your changes with Git:

```bash
# Stage your changes (if you edited README)
git add README.md

# Or stage your new file (if you created a file)
git add YOUR-NAME.txt

# Commit with a descriptive message
git commit -m "Add YOUR-NAME to repository"
```

**Commit Message Tips:**
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Start with a capital letter

---

### Step 6: Push Your Changes

Send your changes to GitHub:

```bash
git push origin add-my-name
```

**What's happening?** You're uploading your local commits to your GitHub fork.

---

### Step 7: Create a Pull Request

1. Go to **your fork** on GitHub
2. You should see a banner saying "Compare & pull request" - click it!
3. Add a title: "Add [Your Name] to contributors"
4. Add a description explaining your changes
5. Click **Create pull request**

**Congratulations!** You've just created your first pull request!

---

## Challenge Exercises

Once you've completed the basic workflow, try these challenges:

### Challenge 1: Add Your Name
Add your name to the "Participants" section below via a PR.

### Challenge 2: Create Multiple Files
Create 2-3 different files and commit them separately with good commit messages.

### Challenge 3: Collaborate
Review someone else's pull request and leave a constructive comment.

### Challenge 4: Fix Something
Find a typo or add additional information to the README via a PR.

---

## Workshop Participants

Add your name here via PR!

- Zeeshan Babul (Workshop Organizer)
<!-- Add your name below this line -->

---

## Git Command Cheat Sheet

| Command | Description |
|---------|-------------|
| `git clone <url>` | Download a repository |
| `git status` | Check the status of your changes |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git push origin <branch>` | Push commits to GitHub |
| `git pull origin main` | Get latest changes from main |
| `git checkout -b <branch>` | Create and switch to new branch |
| `git branch` | List all branches |

---

## Troubleshooting

### "Permission denied" error
- Make sure you cloned **your fork**, not the original repository
- Check that you're logged into Git: `git config user.name` and `git config user.email`

### "Merge conflict" error
- Don't panic! Merge conflicts are normal
- Pull the latest changes: `git pull origin main`
- Git will mark the conflicts in your files
- Edit the files to resolve conflicts, then commit

### Need to configure Git?
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Best Practices

1. **Commit Often:** Make small, frequent commits with clear messages
2. **Pull Before Push:** Always pull the latest changes before pushing
3. **Use Branches:** Never commit directly to main
4. **Write Clear PR Descriptions:** Help reviewers understand your changes
5. **Review Your Changes:** Always check `git status` and `git diff` before committing

---

## Additional Resources

- [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

## Contributing

This is a workshop repository! Feel free to:
- Add your name to the participants list
- Suggest improvements via pull requests
- Help others in their learning journey
- Share tips and tricks you discover

---

## Questions?

If you have any questions during the workshop, please:
- Raise your hand for immediate help
- Open an issue on this repository
- Reach out to the workshop organizers

---

## License

This repository is for educational purposes as part of the UCI Data Science GitHub Workshop.

---

**Happy Coding!**
