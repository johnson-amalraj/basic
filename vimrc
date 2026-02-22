"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               
"               
"               ██╗   ██╗██╗███╗   ███╗██████╗  ██████╗
"               ██║   ██║██║████╗ ████║██╔══██╗██╔════╝
"               ██║   ██║██║██╔████╔██║██████╔╝██║     
"               ╚██╗ ██╔╝██║██║╚██╔╝██║██╔══██╗██║     
"                ╚████╔╝ ██║██║ ╚═╝ ██║██║  ██║╚██████╗
"                 ╚═══╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
"               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""              
" curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""              
" Highlight 'FIXME' in a specific color
" highlight Todo ctermfg=blue ctermbg=none
" autocmd Syntax * syn match Todo "\<FIXME\>"

" Ensure compatibility
set nocompatible

" Encoding settings
set encoding=utf-8

" Background
set background=dark

" Syntax: <font_name>\ <weight>\ <size>
set guifont=Monospace\ Regular\ 10

" For all text files set 'textwidth' to 78 characters.
autocmd FileType text setlocal textwidth=78

" Colorscheme (improved for visibility)
colorscheme molokai 

" Line numbering and cursor settings
set number
set relativenumber

" Customize the cursor line and column highlighting to match the Molokai color scheme
highlight CursorLine cterm=bold ctermbg=235 guibg=#3a3a3a
highlight CursorColumn cterm=bold ctermbg=235 guibg=#3a3a3a
set cursorline
set cursorcolumn

" Tabs and indentation
set tabstop=2
set shiftwidth=2
set expandtab
set autoindent
" set smartindent

" Search settings
set hlsearch
set incsearch
" set ignorecase
set smartcase

" Backup and swap files
set nobackup
set nowritebackup
set noswapfile
set scrolloff=3
set wrap

" Directory
set autochdir

" Mouse support
set mouse=a

" Miscellaneous quality-of-life improvements
set wildmenu
set wildmode=longest:list,full
set showcmd

" Key mappings
" save the files
nnoremap <C-w> :w<CR>

" split open
nnoremap <C-s> :sp<CR>

" You can split the window in Vim by typing :split or :vsplit.
" Navigate the split view easier by pressing CTRL+j, CTRL+k, CTRL+h, or CTRL+l.
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" Resize split windows using arrow keys by pressing:
" CTRL+UP, CTRL+DOWN, CTRL+LEFT, or CTRL+RIGHT.
noremap <c-up> <c-w>+
noremap <c-down> <c-w>-
noremap <c-left> <c-w>>
noremap <c-right> <c-w><

" Map the F4 key to toggle the menu, toolbar, and scroll bar.
" <Bar> is the pipe character.
" <CR> is the enter key.
nnoremap <F4> :if &guioptions=~#'mTr'<Bar>
               \set guioptions-=mTr<Bar>
               \else<Bar>
               \set guioptions+=mTr<Bar>
               \endif<CR>

" NERDTree configuration
let NERDTreeShowHidden=1
nnoremap <F2> :NERDTreeToggle<CR>

" Go to definition
nnoremap <silent> gd :LspDefinition<CR>

" Show references
nnoremap <silent> gr :LspReferences<CR>

" Hover info
nnoremap <silent> K :LspHover<CR>

" Rename symbol
nnoremap <silent> <leader>rn :LspRename<CR>

" Signature help
nnoremap <silent> <leader>sh :LspSignatureHelp<CR>

" Folding : verilog_systemverilog
set foldenable
set foldmethod=syntax
let g:verilog_syntax_fold_lst = "task,function"

" Statusline
set laststatus=2 
set noshowmode
let g:lightline = {
  \ 'colorscheme': 'one',
  \ 'active': {
  \   'left': [ [ 'mode', 'paste' ],
  \             [ 'readonly', 'filename', 'modified' ] ],
  \   'right': [ [ 'lineinfo' ],
  \              [ 'percent' ],
  \              [ 'fileformat' ],
  \              [ 'charvaluehex' ],
  \              [ 'filetype' ],
  \              [ 'fileencoding' ]]
  \ },
  \ 'component_expand': {
  \   'linter_errors': 'lightline#linter#errors',
  \   'linter_warnings': 'lightline#linter#warnings',
  \ },
  \ 'component_type': {
  \   'linter_errors': 'error',
  \   'linter_warnings': 'warning',
  \ },
  \ 'tabline': {
  \   'left': [ ['buffers'] ],
  \   'right': [ ['close'] ]
  \ },
  \ 'component': {
  \   'fileformat': '%{&fileformat}',
  \   'filename': '%F',
  \   'filetype': '%{&filetype}'
  \ }
  \ }

filetype plugin indent on
 syntax on
 augroup Systemverilog
   autocmd!
   autocmd FileType systemverilog setlocal omnifunc=syntaxcomplete#Complete foldmethod=indent
 augroup END
" :help ins-completion.

"----------------------------
" LSP Configuration
"----------------------------

" Use svls if:
" You prefer a language server written in Rust.
" You are looking for a straightforward SystemVerilog language server.
if executable('svls')
  au User lsp_setup call lsp#register_server({
      \ 'name': 'svls',
      \ 'cmd': {server_info->['svls']},
      \ 'whitelist': ['systemverilog']
      \ })
endif

" Use verible-verilog-ls if:
" You want additional tools and features provided by the Verible suite.
" You are interested in code formatting and other advanced features.
 if executable('verible-verilog-ls')
   au User lsp_setup call lsp#register_server({
       \ 'name': 'verible-verilog-ls',
       \ 'cmd': {server_info->['verible-verilog-ls']},
       \ 'whitelist': ['systemverilog']
       \ })
 endif

" " systemverilog filetype
" autocmd BufRead,BufNewFile *.sv set filetype=systemverilog

"----------------------------
" Snippet Integration
"----------------------------
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"

"----------------------------
" Asyncomplete Settings
"----------------------------
let g:asyncomplete_auto_popup = 1
autocmd! CompleteDone * if pumvisible() == 0 | pclose | endif

" Enable completion using asyncomplete
autocmd! CompleteDone * if pumvisible() == 0 | pclose | endif

" ========== Rainbow Parentheses ==========
let g:rainbow_active = 1

" ========== Gitguttter ==========
let g:gitgutter_sign_added = '+'
let g:gitgutter_sign_modified = '~'
let g:gitgutter_sign_removed = '-'

call plug#begin('~/.vim/plugged')

  " NERDTree
  Plug 'preservim/nerdtree'

  " Folding, Indent, Syntax, Tags, Compilation Error
  Plug 'vhda/verilog_systemverilog.vim' 

  " Status Line 
  Plug 'itchyny/lightline.vim' 

  " LSP Client 
  Plug 'prabirshrestha/vim-lsp'

  " Auto-installer for language servers (optional)
  Plug 'mattn/vim-lsp-settings'

  " TODO npm install -g hdl-language-server

  " Autocompletion (optional but recommended)
  Plug 'prabirshrestha/asyncomplete.vim'
  Plug 'prabirshrestha/asyncomplete-lsp.vim'

  " Optional UI plugins
  Plug 'airblade/vim-gitgutter' " Git diff markers

  " Parenthesis highlighter
  Plug 'luochen1990/rainbow'

  " Linting & Diagonositics TODO Need to explore this
  Plug 'dense-analysis/ale'

  " UltiSnips configured
  Plug 'SirVer/ultisnips'
  Plug 'honza/vim-snippets'

  " Matchit: For better code navigation in SystemVerilog, consider:
  Plug 'tmhedberg/matchit'

  " Tagbar: For code structure navigation:
  Plug 'preservim/tagbar'

  " Supertab: For tab-based completion:
  Plug 'ervandew/supertab'

  " Indent Guides: Visualize indentation levels:
  Plug 'Yggdroot/indentLine'

call plug#end()

" TODO
" Need to add support for below item using verilog_systemverilog
"  * Omni completion.
"  * Matchit settings to support Verilog 2001 and SystemVerilog.
"  * Error format definitions for common Verilog tools.
"  * Commands for code navigation.
" Other plugins for verilog_systemverilog.vim
"  - Matchit
"  - Supertab
"  - Tagbar

" Highlight ERROR
syntax match Error /\(UVM_ERROR\|\*E\|-E-\)/
highlight Error ctermfg=Red guifg=Red

" Highlight WARNING
syntax match Warn /\(UVM_WARNING\|\*W\|-W-\)/
highlight Warn ctermfg=Yellow guifg=Yellow

" Highlight FATAL
syntax match Fatal /\(UVM_FATAL\|\*F\|-F-\)/
highlight Fatal ctermfg=Magenta guifg=Magenta

" Highlight TEST_FAIL
syntax match TestFailed /\(TEST_FAILED\|TEST_FAIL\)/
highlight TestFailed ctermfg=Red guifg=Red

" Highlight TEST_PASS
syntax match TestPassed /\(TEST_PASSED\|TEST_PASS\)/
highlight TestPassed ctermfg=Green guifg=Green
