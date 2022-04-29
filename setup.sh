mkdir -p deps
cd deps
if [ -z "$GITHUB_ACTIONS" ]
then
    git clone https://github.com/terminal-labs/epython-wip.git
    git clone https://github.com/terminal-labs/epy-lib-wip.git
    git clone https://github.com/terminal-labs/epy-setup-wip.git 
    git clone https://github.com/terminal-labs/job-light-runner.git
else 
   git clone git@github.com:terminal-labs/epython-wip.git
   git clone git@github.com:terminal-labs/epy-lib-wip.git
   git clone git@github.com:terminal-labs/epy-setup-wip.git   
   git clone git@github.com:terminal-labs/job-light-runner.git
fi
pip install -e epython-wip
pip install -e epy-lib-wip
pip install -e epy-setup-wip
pip install -e job-light-runner
cd ..

mkdir -p runners
cd runners
if [ -z "$GITHUB_ACTIONS" ]
then
   git clone https://github.com/terminal-labs/runner-compilepython-wip.git
else    
   git clone git@github.com:terminal-labs/runner-compilepython-wip.git
fi
pip install -e runner-compilepython-wip
