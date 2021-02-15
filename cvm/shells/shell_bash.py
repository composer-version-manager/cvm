class ShellBash:
    NAME = 'bash'

    @staticmethod
    def get_hook() -> str:
        cvm_path = 'cvm'
        return f'''
            _cvm_hook() {{
                local previous_exit_status=$?;
                trap -- '' SIGINT;
                eval "$({cvm_path} scan bash)";
                trap - SIGINT;
                return $previous_exit_status;
            }}
            if ! [[ "${{PROMPT_COMMAND:-}}" =~ _cvm_hook ]]; then
                PROMPT_COMMAND="_cvm_hook{{PROMPT_COMMAND:+;$PROMPT_COMMAND}}"
            fi
        '''
