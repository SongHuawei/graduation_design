"use strict";
var element = document.querySelector('.overflow');
var timer;

// 检查元素的宽度是否小于文本的宽度
if (element.offsetWidth < element.scrollWidth) {
    // 如果文本已经溢出了元素的可见区域，则添加交互效果
    element.addEventListener('mouseenter', function () {
        // 设置一个2秒的定时器，在定时器到期后展开元素
        timer = setTimeout(function () {
            element.style.overflow = 'visible';
            element.style.whiteSpace = 'normal';
        }, 2000);
    });
    element.addEventListener('mouseleave', function () {
        // 清除定时器
        clearTimeout(timer);
        element.style.overflow = 'hidden';
        element.style.whiteSpace = 'nowrap';
    });
    element.addEventListener('mousemove', function (event) {
        // 鼠标移动时清除定时器
        clearTimeout(timer);
        // 如果鼠标悬停了2秒钟，则展开元素
        timer = setTimeout(function () {
            element.style.overflow = 'visible';
            element.style.whiteSpace = 'normal';
        }, 2000);
    });
}
