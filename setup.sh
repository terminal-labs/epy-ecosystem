mkdir -p deps
cd deps
git clone git@github.com:terminal-labs/epython-wip.git
git clone git@github.com:terminal-labs/epy-lib-wip.git
git clone git@github.com:terminal-labs/epy-setup-wip.git
git clone git@github.com:terminal-labs/job-light-runner.git
pip install -e epython-wip
pip install -e epy-lib-wip
pip install -e epy-setup-wip
pip install -e job-light-runner
cd ..

mkdir -p examples/runners
cd examples/runners
git git@github.com:terminal-labs/runner-compilepython-wip.git
pip install -e runner-compilepython-wip
cd ../..

cp -r examples/plugins plugins
