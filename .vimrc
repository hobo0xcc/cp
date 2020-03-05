scriptencoding utf-8
set encoding=utf-8
set nocompatible
set number
set title
set ruler
set autoindent
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set backspace=indent,eol,start
set mouse=a
set clipboard=unnamed
set wrap

syntax on
colorscheme molokai
set noswapfile
set t_Co=256
set visualbell
set noerrorbells
set nobackup
set noundofile
set relativenumber
set scrolloff=999
set background=dark
set shortmess+=I
set ignorecase

nnoremap <C-a> G$vgg
nnoremap <S-Up> 10k
nnoremap <S-Down> 10j
nnoremap <space><Right> :bnext<CR>
nnoremap <space><Left> :bprev<CR>
tnoremap <C-c> <C-\><C-n>
nnoremap <space>/ :vsplit<CR>
nnoremap <space>- :split<CR>
nnoremap <space>a <C-w>h
nnoremap <space>w <C-w>k
nnoremap <space>s <C-w>j
nnoremap <space>d <C-w>l
nnoremap <space><space> :Deol<CR>
nnoremap <Leader>t :FZF<CR>
nnoremap <Leader>h :Rg<CR>
nnoremap <Leader>r :!make<CR>
nnoremap <Leader>e :!make init<CR>

call plug#begin('~/VimPlugin')

Plug 'Shougo/deol.nvim'
Plug 'cohama/lexima.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'SirVer/ultisnips'

call plug#end()

" Plugin settings
let g:UltiSnipsSnippetDirectories=["/Users/hobo/Develop/cp/snippets"]
let g:UltiSnipsExpandTrigger="<tab>"
