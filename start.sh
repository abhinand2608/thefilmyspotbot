if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/abhinand2608/thefilmyspotbot.git /thefilmyspotbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /thefilmyspotbot
fi
cd /thefilmyspotbot
pip3 install -U -r requirements.txt
echo "Starting ThefilmyspotBot ✅...."
python3 bot.py
