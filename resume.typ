#import "@preview/cuti:0.2.1": show-cn-fakebold
#show: show-cn-fakebold
#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommended resume text size is from `10pt` to `12pt`
// #set text(
//   size: 12pt,
// )

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/  

#set par(justify: true)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}

#let fontbold(s,t) = {text(size:s,weight: "bold")[#t]}

= Nai Long
#place(top+right,[#image("picture.jpeg",width: 7.5%, height: auto)])
#link("xxxx\@gmail.com")[xxxx\@gmail.com]
#link("https://xxx.github.io")[https://xxx.github.io]
#link("https://github.com/xxx")[https://github.com/xxx]
== Education Experience 
#chiline()
*XXX University* #h(1fr) 2023/09 -- 2026/06 \
Recommended for exemption

*XXX University* #h(1fr) 2019/09 -- 2023/06 \
First-class scholarship, outstanding student


== Work Experience 
#chiline()
*xxx* #h(1fr) 2023/09 -- 2026/06 \
*Summary*:xxxx- xxx

- xxx


== Research Experience 
#chiline()
*xxx* #h(1fr) 2023/09 -- 2026/06 \
- xxx

- xxx


== Project Experience 
#chiline()
*xxx* #h(1fr) 2023/09 -- 2026/06 \
- xxx

- xxx


== Skills 
#chiline()
- *programming language*: cpp, golang
- *tools*: docker
- *english*: cet-6

