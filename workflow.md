MY ASTR-119 WORKFLOW

TERMINAL SHORTCUTS (defined in ~/.zshrc)
- astr119: go to ~/astr119 and activate the astr119 conda environment
- gsync "message": add, commit, pull from the class repo, push to my fork

ADDING THE SHORTCUTS (on a new computer)
1. In the terminal, run:  open -e ~/.zshrc
2. Paste these lines at the very bottom:

    alias astr119='cd ~/astr119 && conda activate astr119'

    gsync() {
      git add -A
      git commit -m "${1:-sync}"
      git pull --no-rebase --no-edit upstream main && git push
    }

3. Save with Cmd+S, then in the terminal run:  source ~/.zshrc
4. One time only, connect the class repo:
    git remote add upstream https://github.com/kbundy/astr119-fall2026

STARTING AN ASSIGNMENT
    astr119
    gsync ""    #get the professor's new files
    cp module-N/thing_starter.py module-N/thing.py   #work in my own copy, not the starter
    gsync "pod N: starting copy"
- Check the first line of the file: NO-AI means no agent.
- Never edit the professor's _starter files. (prevents merge issues)

EVERY TIME BEFORE THE AGENT CHANGES CODE
    gsync "before the agent"

CHECKING THAT EVERYTHING IS SYNCED
    git status      "up to date" + "nothing to commit" = all pushed


END OF A SESSION
- /export the Claude Code transcript.
- Write the AI-use note.
