package shell

var Zsh = zshShell{}

type zshShell struct{}

func (sh zshShell) Hook() string {
	return `
	_cvm_hook() {
		trap -- '' SIGINT;
		eval "$(cvm scan zsh)";
		trap - SIGINT;
	}
	typeset -ag precmd_functions;
	if [[ $precmd_functions != *_cvm_hook* ]]; then
		precmd_functions=( _cvm_hook ${precmd_functions[@]} )
	fi
	typeset -ag chpwd_functions;
	if [[ $chpwd_functions != *_cvm_hook* ]]; then
  		chpwd_functions=( _cvm_hook ${chpwd_functions[@]} )
	fi
	`
}
