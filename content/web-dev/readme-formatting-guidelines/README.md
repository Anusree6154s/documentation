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




## Credits
1. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
2. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting
3. 
