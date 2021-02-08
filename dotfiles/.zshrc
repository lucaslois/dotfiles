# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

source ~/antigen.zsh

################################################################################################
# Antigen
################################################################################################

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

antigen theme romkatv/Powerlevel10k

antigen apply

################################################################################################
# Aliases
################################################################################################
alias vim="nvim"
alias edithost="sudo subl /etc/hosts"

export TERM=vt100
export TERM=xterm-256color
export TZ=":America/Argentina/Buenos_Aires"

################################################################################################
# Plugins
################################################################################################

#Autojump
[[ -s /home/lucasl/.autojump/etc/profile.d/autojump.sh ]] && source /home/lucasl/.autojump/etc/profile.d/autojump.sh

# FuzzyFinder
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
