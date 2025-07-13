<div align='center'>
  <h2>Blog Website</h2>
<img src='https://github.com/user-attachments/assets/3d34a9ec-e32a-459f-86df-61a71ba71425' width=500/>
</div>


### Techstack
1. Jekyll: Website skeleton
2. SASS: Styling

### To Run Locally
1. Clone website to your IDE by running `git clone https://github.com/Anusree6154s/documentation.git`
2. Run `bundle exec jekyll serve` or `npm start` in terminal
3. Visit the url that appears in your terminal
> **To stop application**: Press `Ctrl+C` and then press y

<br>
<br>

<div style="border:1px solid #ccc; padding:10px; border-radius:5px">

### Note to self
Process of re-setting up project locally
- **Install ruby**: 
  - [https://rubyinstaller.org/](https://rubyinstaller.org/)
  - Download the latest **Ruby+Devkit** version for Windows.
  - GPT asked to do this: `Install with all defaults, and check the box that says "Add Ruby executables to your PATH".`. But couldn't do it and nothing went wrong
  - After install, it may ask to run `ridk install`. Choose option `3` (install MSYS2, MINGW, etc.).
- **Install Bundler**
  - Open command prompt (not bash terminal)
  - Run `ruby -v` and `gem install bundler`
  - Get the location fo ruby by running `where ruby`. If path is `C:\Ruby34-x64\bin\ruby.exe` then run this in bash terminal to add the bath to `.bashrc`:
    ```
    echo 'export PATH="/c/Ruby34-x64/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```
- **Run bundler in bash**
  - In terminal, run `bundle install` and `npm start`
</div>