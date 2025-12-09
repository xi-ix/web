// 1. 获取元素
let button = document.getElementById("myButton");
let text = document.getElementById("myText");

// 2. 添加点击事件
button.addEventListener("click", function() {
    // 3. 修改元素内容
    text.textContent = "文本被改变了！";
    text.style.color = "red";
  
    // 4. 创建新元素
    let newElement = document.createElement("div");
    newElement.textContent = "这是新添加的内容";
    console.log(newElement);
    document.body.appendChild(newElement);
});

//更换标题
const myheading = document.getElementById("head1main");
myheading.textContent="hello world!";

alert("hello!"); //  弹出提示框，显示"hello!"