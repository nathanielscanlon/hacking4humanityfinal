# Edited Albumy For Hate Prevention

Original code from: https://github.com/greyli/albumy.git
The following is a repo for Nathaniel Scanlon and Adam Johnson's Hacking4Humanity 2025 Project.
We adapted the code from a fake socical media as seen above that did not have
any hate protections. We then implemented an AI scanner to detect hate speech and falg it. To prevent censoring free speech
we allowed users to customize their own protections so they could filter hate speech if they choose.
Futhermore, we added carious parental controls and resources to help deter the spread of hate speech.

Changes:
The files albumy/templates/main/confirm_hate_speech.html and albumy/templates/user/settings/hate_safety.html were created soley by us. 
In albumy/utils.py 109 - 133 were programmed by us.
In albumy/blueprints/main.py 383-416 were programmed by us.
IN albumy/forms/user.py  71-80 were programmed by us.
In albumy/blueprints/user.py 220-231 were programmed by us.
Other files weere edited by us, but they were used to make fake accounts on the 
site. Furthermore, other html files were edited to display our settings. However,
all relevant files to the way the hate prevention works and the site is displayed
are above.

