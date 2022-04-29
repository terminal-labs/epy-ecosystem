mkdir -p deps
cd deps
git clone git@github.com:terminal-labs/epython-wip.git
git clone git@github.com:terminal-labs/epy-lib-wip.git
git clone git@github.com:terminal-labs/epy-setup-wip.git
git clone https://github.com/terminal-labs/job-light-runner.git
pip install -e epython-wip
pip install -e epy-lib-wip
pip install -e epy-setup-wip
pip install -e job-light-runner
cd ..

mkdir -p runners
cd runners
git clone git@github.com:terminal-labs/runner-compilepython-wip.git
pip install -e runner-compilepython-wip
