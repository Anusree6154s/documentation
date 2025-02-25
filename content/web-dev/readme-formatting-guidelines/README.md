---
title: Readme files formatting guide
date: Oct 23, 2024
layout: post
excerpt: Comprehensive Guide to Formatting README Files
permalink: readme-formatting-guidelines
---

## Readme Formatting Guidelines/Rules
- [Majority guidelines](https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796)
- [Image alignment/resize guidelines](https://gist.github.com/kigiri/4b1d64eba2d465a2ffc1342a0e9e7d6f)


## Github readme formatting styles put together by me


### **1. Bolden words using asterisks (`**bold**` or `__bold__`)**  
   - ```md
     **This is bold text**
     __This is bold text__
     ```  
   - **This is bold text**  
     __This is bold text__  



### **2. Italicize words using asterisks (`*italic*` or `_italic_`)**  
   - ```md
     *This text is italicized*
     _This text is italicized_
     ```  
   - *This text is italicized*  
     _This text is italicized_  



### **3. Strikethrough text using tildes (`~~strikethrough~~`)**  
   - ```md
     ~~This was mistaken text~~
     ```  
   - ~~This was mistaken text~~  



### **4. Combine bold and italic (`**bold _italic_**`)**  
   - ```md
     **This text is _extremely_ important**
     ```  
   - **This text is _extremely_ important**  



### **5. Apply both bold and italic to text (`***bold italic***`)**  
   - ```md
     ***All this text is important***
     ```  
   - ***All this text is important***  



### **6. Add subscript text (`<sub>subscript</sub>`)**  
   - ```md
     This is a <sub>subscript</sub> text
     ```  
   - This is a <sub>subscript</sub> text  



### **7. Add superscript text (`<sup>superscript</sup>`)**  
   - ```md
     This is a <sup>superscript</sup> text
     ```  
   - This is a <sup>superscript</sup> text  



### **8. Underline text (`<ins>underline</ins>`)**  
   - ```md
     This is an <ins>underlined</ins> text
     ```  
   - This is an <ins>underlined</ins> text  



### **9. Quote text using `>` (blockquotes)**  
   - ```md
     > This is a quote
     ```  
   - > This is a quote  



### **10. Inline code using backticks (`\`code\``)**  
   - ```md
     Use `git status` to check changes.
     ```  
   - Use `git status` to check changes.  



### **11. Multi-line code blocks using triple backticks (` ``` `)**  
   - ```md
            ```
            git status
            git add .
            git commit -m "Commit message"
            ```
     ```  
   -  
     ```
     git status
     git add .
     git commit -m "Commit message"
     ```  



### **12. Display colors using HEX, RGB, or HSL**
> [!WARNING]
> this doesnt seem to be working anywhere. To check later
   - ```md
     `#0969DA`
     `rgb(9, 105, 218)`
     `hsl(212, 92%, 45%)`
     ```  
   - `#0969DA`  
     `rgb(9, 105, 218)`  
     `hsl(212, 92%, 45%)`  
     - `rgb(9, 105, 218)`



### **13. Add links (`[text](URL)`)**  
   - ```md
     [GitHub Pages](https://pages.github.com/)
     ```  
   - [GitHub Pages](https://pages.github.com/)  



### **14. Link to sections (`[#section](#section-name)`)**  
   - ```md
     [Go to Sample Section](#sample-section)
     ```  
   - [Go to Sample Section](#sample-section)  



### **15. Add images (`![alt text](image_url)`)**  
   - ```md
     ![Octocat](https://myoctocat.com/assets/images/base-octocat.svg)
     ```  
   - ![Octocat](https://myoctocat.com/assets/images/base-octocat.svg)  



### **16. Unordered lists using `-`, `*`, or `+`**  
   - ```md
     - Item 1
     * Item 2
     + Item 3
     ```  
   -  
     - Item 1  
     * Item 2  
     + Item 3  



### **17. Ordered lists using numbers (`1. 2. 3.`)**  
   - ```md
     1. First item
     2. Second item
     3. Third item
     ```  
   -  
     1. First item  
     2. Second item  
     3. Third item  



### **18. Nested lists (indenting sub-items)**  
   - ```md
     1. Main item  
        - Sub-item  
          - Sub-sub-item  
     ```  
   -  
     1. Main item  
        - Sub-item  
          - Sub-sub-item  



### **19. Task lists using `- [ ]` (checkboxes)**  
   - ```md
     - [x] Completed task
     - [ ] Pending task
     ```  
   -  
     - [x] Completed task  
     - [ ] Pending task  



### **20. Mention users (`@username`)**  
   - ```md
     @octocat
     ```  
   - @octocat  



### **21. Reference issues & PRs (`#issue-number`)**  
   - ```md
     See issue #123
     ```  
   - See issue #123  



### **22. Add emojis (`:emoji_name:`)**  
   - ```md
     :rocket: :tada:
     ```  
   - 🚀 🎉  



### **23. Add footnotes (`[^1]`)**  
   - It doesnt work in preview. It can only be viewed directly on github
   - ```md
     Here is a footnote[^1].  
      
     [^1]: This is the footnote text.
     ```  
   - Here is a footnote[^1].  

     [^1]: This is the footnote text.  


     



### **24. Alerts (`> [!NOTE]`, `> [!WARNING]`)**  
   - ```md
     > [!NOTE]  
     > This is an important note.  

     > [!WARNING]  
     > This is a warning message.
     ```  
   -  
     > [!NOTE]  
     > This is an important note.  

     > [!WARNING]  
     > This is a warning message.  



### **25. Hide content using HTML comments (`<!-- hidden -->`)**  
   - ```md
     <!-- This content will not appear in the rendered Markdown -->
     ```  



### **26. Escape Markdown formatting using `\`**  
   - ```md
     Let's rename \*our-new-project\* to \*our-old-project\*.
     ```  
   - Let's rename \*our-new-project\* to \*our-old-project\*.  


## Credits
1. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax