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
> [!WARNING]
> Many of the styles here dont work during developemnt. Instead only on github. And this needs to be viewed in github to see the right results: 

### **1. Formatting text**  
|code|result|
|--|--|
|``` **This is bold text using asterisk**```|**This is bold text using asterisk**|
|```  __This is bold text using underscore__```| __This is bold text using underscore__|
|```   *This text is italicized using asterisk*```|  *This text is italicized using asterisk*|
|```  _This text is italicized using underscore_```| _This text is italicized using underscore_|
|``` ~~This is text strikethrouh using tilde~~```|~~This is text strikethrouh using tilde~~|
|```  **This text is _itallic_ and bold in same phrase**```| **This text is _itallic_ and bold in same phrase**|
|``` ***This text is _itallic_ and bold combined***```|***This text is _itallic_ and bold combined***|
|``` This is a <sub>subscript</sub> text```|This is a <sub>subscript</sub> text|
|```  This is a <sup>superscript</sup> text```| This is a <sup>superscript</sup> text*|
|```  This is an <ins>underlined</ins> text```| This is an <ins>underlined</ins> text|
|```  This is `inline` code using backticks```| This is `inline` code using backticks|
|``` ***This text is _itallic_ and bold combined***```|***This text is _itallic_ and bold combined***|
|``` ***This text is _itallic_ and bold combined***```|***This text is _itallic_ and bold combined***|
|``` ***This text is _itallic_ and bold combined***```|***This text is _itallic_ and bold combined***|
|``` ***This text is _itallic_ and bold combined***```|***This text is _itallic_ and bold combined***|




- ```md
  > This is a quote using blockquotes
  ```  
> This is a quote using blockquotes




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
   
   - ```md
     - Here is a simple footnote[^1].
     - A footnote can also have multiple lines[^2].   
     - You can also use words, to fit your writing style more closely[^note].
      
      [^1]: My reference.
      [^2]: Every new line should be prefixed with 2 spaces.  
        This allows you to have a footnote with multiple lines.
      [^note]:
          Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
          This footnote also has been made with a different syntax using 4 spaces for new lines.
     ```  
- Here is a simple footnote[^1].
- A footnote can also have multiple lines[^2].  
- You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.


     



### **24. Alerts (`> [!NOTE]`, `> [!WARNING]`)**  
   - ```md
      > [!NOTE]
      > Useful information that users should know, even when skimming content.
      
      > [!TIP]
      > Helpful advice for doing things better or more easily.
      
      > [!IMPORTANT]
      > Key information users need to know to achieve their goal.
      
      > [!WARNING]
      > Urgent info that needs immediate user attention to avoid problems.
      
      > [!CAUTION]
      > Advises about risks or negative outcomes of certain actions.
     ```  
 
   > [!NOTE]
   > Useful information that users should know, even when skimming content.
   
   > [!TIP]
   > Helpful advice for doing things better or more easily.
   
   > [!IMPORTANT]
   > Key information users need to know to achieve their goal.
   
   > [!WARNING]
   > Urgent info that needs immediate user attention to avoid problems.
   
   > [!CAUTION]
   > Advises about risks or negative outcomes of certain actions. 



### **25. Hide content using HTML comments (`<!-- hidden -->`)**  
   - ```md
     <!-- This content will not appear in the rendered Markdown -->
     ```  



### **26. Escape Markdown formatting using `\`**  
   - ```md
     Let's rename \*our-new-project\* to \*our-old-project\*.
     ```  
   - Let's rename \*our-new-project\* to \*our-old-project\*.

Sure! Here’s the rewritten content in your requested format:  

---

### 1. **Create a Table using Pipes (`|`) and Hyphens (`-`)**  
   - ```md  
     | First Header  | Second Header |  
     | ------------- | ------------- |  
     | Content Cell  | Content Cell  |  
     | Content Cell  | Content Cell  |  
     ```  
   -  
     | First Header  | Second Header |  
     | ------------- | ------------- |  
     | Content Cell  | Content Cell  |  
     | Content Cell  | Content Cell  |  

---

### 2. **Tables Do Not Require Perfect Alignment**  
   - ```md  
     | Command  | Description                           |  
     | ---      | ---                                   |  
     | git status | List all new or modified files       |  
     | git diff | Show file differences not yet staged |  
     ```  
   -  
     | Command  | Description                           |  
     | ---      | ---                                   |  
     | git status | List all new or modified files       |  
     | git diff | Show file differences not yet staged |  

---

### 3. **Use Inline Code Blocks (`) Inside Tables**  
   - ```md  
     | Command     | Description                                |  
     | ---        | ---                                        |  
     | `git status` | List all *new or modified* files         |  
     | `git diff`   | Show file differences that **haven't been** staged |  
     ```  
   -  
     | Command     | Description                                |  
     | ---        | ---                                        |  
     | `git status` | List all *new or modified* files         |  
     | `git diff`   | Show file differences that **haven't been** staged |  

---

### 4. **Align Table Text to Left, Center, or Right**  
   - ```md  
     | Left-aligned | Center-aligned | Right-aligned |  
     | :---        |     :---:      |          ---: |  
     | git status  | git status     | git status    |  
     | git diff    | git diff       | git diff      |  
     ```  
   -  
     | Left-aligned | Center-aligned | Right-aligned |  
     | :---        |     :---:      |          ---: |  
     | git status  | git status     | git status    |  
     | git diff    | git diff       | git diff      |  

---

### 5. **Display a Pipe (`|`) Inside a Table Cell**  
   - ```md  
     | Name     | Character |  
     | ---      | ---       |  
     | Backtick | `         |  
     | Pipe     | \|        |  
     ```  
   -  
     | Name     | Character |  
     | ---      | ---       |  
     | Backtick | `         |  
     | Pipe     | \|        |  

### 1. **Create a Collapsed Section using `<details>`**  
   - ```md  
     <details>  
     <summary>Click to expand</summary>  
       
     This text is hidden by default and will be revealed when clicked.  

     </details>  
     ```  
   -  
     <details>  
     <summary>Click to expand</summary>  
       
     This text is hidden by default and will be revealed when clicked.  

     </details>  

---

### 2. **Add a Header, Text, or Code Block Inside a Collapsed Section**  
   - ```md  
     <details>  
     <summary>Tips for collapsed sections</summary>  

     ### You can add a header  

     You can add text within a collapsed section.  

     You can add an image or a code block, too.  

     ```ruby  
     puts "Hello World"  
     ```  

     </details>  
     ```  
   -  
     <details>  
     <summary>Tips for collapsed sections</summary>  

     ### You can add a header  

     You can add text within a collapsed section.  

     You can add an image or a code block, too.  

     ```ruby  
     puts "Hello World"  
     ```  

     </details>  

---

### 3. **Make a Collapsed Section Open by Default**  
   - ```md  
     <details open>  
     <summary>Always visible section</summary>  

     This section starts open by default.  

     </details>  
     ```  
   -  
     <details open>  
     <summary>Always visible section</summary>  

     This section starts open by default.  

     </details>  
### 1. **Create a Mermaid Diagram**  
   - ```md  
     ```mermaid  
     graph TD;  
         A-->B;  
         A-->C;  
         B-->D;  
         C-->D;  
     ```  
     ```  
   -  
     ```mermaid  
     graph TD;  
         A-->B;  
         A-->C;  
         B-->D;  
         C-->D;  
     ```  

---

### 2. **Check the Mermaid Version in Use**  
   - ```md  
     ```mermaid  
     info  
     ```  
     ```  
   -  
     ```mermaid  
     info  
     ```  

---

### 3. **Create a GeoJSON Map**  
   - ```md  
     ```geojson  
     {  
       "type": "FeatureCollection",  
       "features": [  
         {  
           "type": "Feature",  
           "id": 1,  
           "properties": {  
             "ID": 0  
           },  
           "geometry": {  
             "type": "Polygon",  
             "coordinates": [  
               [  
                   [-90,35],  
                   [-90,30],  
                   [-85,30],  
                   [-85,35],  
                   [-90,35]  
               ]  
             ]  
           }  
         }  
       ]  
     }  
     ```  
     ```  
   -  
     ```geojson  
     {  
       "type": "FeatureCollection",  
       "features": [  
         {  
           "type": "Feature",  
           "id": 1,  
           "properties": {  
             "ID": 0  
           },  
           "geometry": {  
             "type": "Polygon",  
             "coordinates": [  
               [  
                   [-90,35],  
                   [-90,30],  
                   [-85,30],  
                   [-85,35],  
                   [-90,35]  
               ]  
             ]  
           }  
         }  
       ]  
     }  
     ```  

---

### 4. **Create a TopoJSON Map**  
   - ```md  
     ```topojson  
     {  
       "type": "Topology",  
       "transform": {  
         "scale": [0.0005000500050005, 0.00010001000100010001],  
         "translate": [100, 0]  
       },  
       "objects": {  
         "example": {  
           "type": "GeometryCollection",  
           "geometries": [  
             {  
               "type": "Point",  
               "properties": {"prop0": "value0"},  
               "coordinates": [4000, 5000]  
             },  
             {  
               "type": "LineString",  
               "properties": {"prop0": "value0", "prop1": 0},  
               "arcs": [0]  
             },  
             {  
               "type": "Polygon",  
               "properties": {"prop0": "value0", "prop1": {"this": "that"}},  
               "arcs": [[1]]  
             }  
           ]  
         }  
       },  
       "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]  
     }  
     ```  
     ```  
   -  
     ```topojson  
     {  
       "type": "Topology",  
       "transform": {  
         "scale": [0.0005000500050005, 0.00010001000100010001],  
         "translate": [100, 0]  
       },  
       "objects": {  
         "example": {  
           "type": "GeometryCollection",  
           "geometries": [  
             {  
               "type": "Point",  
               "properties": {"prop0": "value0"},  
               "coordinates": [4000, 5000]  
             },  
             {  
               "type": "LineString",  
               "properties": {"prop0": "value0", "prop1": 0},  
               "arcs": [0]  
             },  
             {  
               "type": "Polygon",  
               "properties": {"prop0": "value0", "prop1": {"this": "that"}},  
               "arcs": [[1]]  
             }  
           ]  
         }  
       },  
       "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]  
     }  
     ```  

---

### 5. **Create an ASCII STL 3D Model**  
   - ```md  
     ```stl  
     solid cube_corner  
       facet normal 0.0 -1.0 0.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 1.0 0.0 0.0  
           vertex 0.0 0.0 1.0  
         endloop  
       endfacet  
       facet normal 0.0 0.0 -1.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 0.0 1.0 0.0  
           vertex 1.0 0.0 0.0  
         endloop  
       endfacet  
       facet normal -1.0 0.0 0.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 0.0 0.0 1.0  
           vertex 0.0 1.0 0.0  
         endloop  
       endfacet  
       facet normal 0.577 0.577 0.577  
         outer loop  
           vertex 1.0 0.0 0.0  
           vertex 0.0 1.0 0.0  
           vertex 0.0 0.0 1.0  
         endloop  
       endfacet  
     endsolid  
     ```  
     ```  
   -  
     ```stl  
     solid cube_corner  
       facet normal 0.0 -1.0 0.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 1.0 0.0 0.0  
           vertex 0.0 0.0 1.0  
         endloop  
       endfacet  
       facet normal 0.0 0.0 -1.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 0.0 1.0 0.0  
           vertex 1.0 0.0 0.0  
         endloop  
       endfacet  
       facet normal -1.0 0.0 0.0  
         outer loop  
           vertex 0.0 0.0 0.0  
           vertex 0.0 0.0 1.0  
           vertex 0.0 1.0 0.0  
         endloop  
       endfacet  
       facet normal 0.577 0.577 0.577  
         outer loop  
           vertex 1.0 0.0 0.0  
           vertex 0.0 1.0 0.0  
           vertex 0.0 0.0 1.0  
         endloop  
       endfacet  
     endsolid  
     ```  

### 1. **Write Inline Mathematical Expressions Using `$`**  
   - ```md  
     This sentence uses `$` delimiters to show math inline: $\sqrt{3x-1}+(1+x)^2$  
     ```  
   -  
     This sentence uses `$` delimiters to show math inline: $\sqrt{3x-1}+(1+x)^2$  

---

### 2. **Write Inline Mathematical Expressions Using `$` with Backticks**  
   - ```md  
     This sentence uses $\` and \`$ delimiters to show math inline: $`\sqrt{3x-1}+(1+x)^2`$  
     ```  
   -  
     This sentence uses $\` and \`$ delimiters to show math inline: $`\sqrt{3x-1}+(1+x)^2`$  

---

### 3. **Write Block Mathematical Expressions Using `$$`**  
   - ```md  
     **The Cauchy-Schwarz Inequality**\  
     $$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$  
     ```  
   -  
     **The Cauchy-Schwarz Inequality**\  
     $$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$  

---

### 4. **Write Block Mathematical Expressions Using `math` Code Blocks**  
   - ```md  
     **The Cauchy-Schwarz Inequality**  
     ```math  
     \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)  
     ```  
     ```  
   -  
     **The Cauchy-Schwarz Inequality**  
     ```math  
     \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)  
     ```  

---

### 5. **Display a Dollar Sign Inside a Math Expression Using `\`**  
   - ```md  
     This expression uses `\$` to display a dollar sign: $`\sqrt{\$4}`$  
     ```  
   -  
     This expression uses `\$` to display a dollar sign: $`\sqrt{\$4}`$  

---

### 6. **Display a Dollar Sign Outside a Math Expression Using `<span>`**  
   - ```md  
     To split <span>$</span>100 in half, we calculate $100/2$  
     ```  
   -  
     To split <span>$</span>100 in half, we calculate $100/2$  

### 1. **Autolink Standard URLs**  
   - ```md  
     Visit https://github.com  
     ```  
   -  
     Visit https://github.com  

---

### 2. **Autolink Issues and Pull Requests Using Full URL**  
   - ```md  
     https://github.com/jlord/sheetsee.js/issues/26  
     ```  
   -  
     https://github.com/jlord/sheetsee.js/issues/26  

---

### 3. **Autolink Issues and Pull Requests Using `#` and Issue Number**  
   - ```md  
     #26  
     ```  
   -  
     #26  

---

### 4. **Autolink Issues and Pull Requests Using `GH-` Prefix**  
   - ```md  
     GH-26  
     ```  
   -  
     GH-26  

---

### 5. **Autolink Issues and Pull Requests Using `Username/Repository#IssueNumber`**  
   - ```md  
     jlord/sheetsee.js#26  
     ```  
   -  
     jlord/sheetsee.js#26  

---

### 6. **Autolink Issues and Pull Requests Using `OrgName/Repository#IssueNumber`**  
   - ```md  
     github-linguist/linguist#4039  
     ```  
   -  
     github-linguist/linguist#4039  

---

### 7. **Autolink Labels from the Same Repository**  
   - ```md  
     https://github.com/github/docs/labels/enhancement  
     ```  
   -  
     https://github.com/github/docs/labels/enhancement  

---

### 8. **Autolink Commit SHAs Using Full Commit URL**  
   - ```md  
     https://github.com/jlord/sheetsee.js/commit/a5c3785ed8d6a35868bc169f07e40e889087fd2e  
     ```  
   -  
     https://github.com/jlord/sheetsee.js/commit/a5c3785ed8d6a35868bc169f07e40e889087fd2e  

---

### 9. **Autolink Commit SHAs Using Short SHA**  
   - ```md  
     a5c3785  
     ```  
   -  
     a5c3785  

---

### 10. **Autolink Commit SHAs Using `User@SHA` Format**  
   - ```md  
     jlord@a5c3785  
     ```  
   -  
     jlord@a5c3785  

---

### 11. **Autolink Commit SHAs Using `Username/Repository@SHA` Format**  
   - ```md  
     jlord/sheetsee.js@a5c3785  
     ```  
   -  
     jlord/sheetsee.js@a5c3785  

---

### 12. **Autolink External Resources with Custom Autolinks**  
   - ```md  
     Example: JIRA-123  
     ```  
   -  
     Example: JIRA-123  




## Credits
1. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
2. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting
3. https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet
