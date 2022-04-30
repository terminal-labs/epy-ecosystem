echo "runnign test track"
START="$(date +%s)"
runnercompilepython runner track
DURATION=$[ $(date +%s) - ${START} ]
echo "done with test track in " ${DURATION}
