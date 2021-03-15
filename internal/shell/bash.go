package shell

var Bash bashShell = bashShell{}

type bashShell struct{}

func (sh bashShell) Hook() string {
	return `
    _cvm_hook() {
        local previous_exit_status=$?;
        trap -- '' SIGINT;
        eval "$("{{.SelfPath}}" hook bash)";
        trap - SIGINT;
        return $previous_exit_status;
    };
    if ! [[ "${PROMPT_COMMAND:-}" =~ _cvm_hook ]]; then
       PROMPT_COMMAND="_cvm_hook${PROMPT_COMMAND:+;$PROMPT_COMMAND}"
    fi
    `
}
