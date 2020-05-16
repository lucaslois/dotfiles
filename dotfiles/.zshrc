source ~/antigen.zsh

antigen use oh-my-zsh

antigen bundle git
antigen bundle heroku
antigen bundle command-not-found
antigen bundle docker
antigen bundle docker-compose
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle npm
antigen bundle nvm
antigen bundle python
antigen bundle tmux
antigen bundle brew

# antigen theme romkatv/powerlevel10k

antigen apply

#Aliases
alias vim="nvim"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

#Autojump
[[ -s /home/lucasl/.autojump/etc/profile.d/autojump.sh ]] && source /home/lucasl/.autojump/etc/profile.d/autojump.sh

# FuzzyFinder
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
