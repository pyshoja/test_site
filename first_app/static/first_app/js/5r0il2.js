window.addComment=function(v){var I,C,h,E=v.document,b={commentReplyClass:"comment-reply-link",commentReplyTitleId:"reply-title",cancelReplyId:"cancel-comment-reply-link",commentFormId:"commentform",temporaryFormId:"wp-temp-form-div",parentIdFieldId:"comment_parent",postIdFieldId:"comment_post_ID"},e=v.MutationObserver||v.WebKitMutationObserver||v.MozMutationObserver,r="querySelector"in E&&"addEventListener"in v,n=!!E.documentElement.dataset;function t(){d(),e&&new e(o).observe(E.body,{childList:!0,subtree:!0})}function d(e){if(r&&(I=g(b.cancelReplyId),C=g(b.commentFormId),I)){I.addEventListener("touchstart",l),I.addEventListener("click",l);var t=function(e){if((e.metaKey||e.ctrlKey)&&13===e.keyCode)return C.removeEventListener("keydown",t),e.preventDefault(),C.submit.click(),!1};C&&C.addEventListener("keydown",t);for(var n,d=function(e){var t=b.commentReplyClass;e&&e.childNodes||(e=E);t=E.getElementsByClassName?e.getElementsByClassName(t):e.querySelectorAll("."+t);return t}(e),o=0,i=d.length;o<i;o++)(n=d[o]).addEventListener("touchstart",a),n.addEventListener("click",a)}}function l(e){var t,n,d=g(b.temporaryFormId);d&&h&&(g(b.parentIdFieldId).value="0",t=d.textContent,d.parentNode.replaceChild(h,d),this.style.display="none",n=(d=(n=g(b.commentReplyTitleId))&&n.firstChild)&&d.nextSibling,d&&d.nodeType===Node.TEXT_NODE&&t&&(n&&"A"===n.nodeName&&n.id!==b.cancelReplyId&&(n.style.display=""),d.textContent=t),e.preventDefault())}function a(e){var t=g(b.commentReplyTitleId),n=t&&t.firstChild.textContent,d=this,o=m(d,"belowelement"),i=m(d,"commentid"),r=m(d,"respondelement"),t=m(d,"postid"),n=m(d,"replyto")||n;o&&i&&r&&t&&!1===v.addComment.moveForm(o,i,r,t,n)&&e.preventDefault()}function o(e){for(var t=e.length;t--;)if(e[t].addedNodes.length)return void d()}function m(e,t){return n?e.dataset[t]:e.getAttribute("data-"+t)}function g(e){return E.getElementById(e)}return r&&"loading"!==E.readyState?t():r&&v.addEventListener("DOMContentLoaded",t,!1),{init:d,moveForm:function(e,t,n,d,o){var i=g(e);h=g(n);var r,l,a,m,c,s=g(b.parentIdFieldId),y=g(b.postIdFieldId),p=(c=g(b.commentReplyTitleId))&&c.firstChild,u=p&&p.nextSibling;if(i&&h&&s){void 0===o&&(o=p&&p.textContent),m=h,e=b.temporaryFormId,n=g(e),c=(c=g(b.commentReplyTitleId))?c.firstChild.textContent:"",n||((n=E.createElement("div")).id=e,n.style.display="none",n.textContent=c,m.parentNode.insertBefore(n,m)),d&&y&&(y.value=d),s.value=t,I.style.display="",i.parentNode.insertBefore(h,i.nextSibling),p&&p.nodeType===Node.TEXT_NODE&&(u&&"A"===u.nodeName&&u.id!==b.cancelReplyId&&(u.style.display="none"),p.textContent=o),I.onclick=function(){return!1};try{for(var f=0;f<C.elements.length;f++)if(r=C.elements[f],l=!1,"getComputedStyle"in v?a=v.getComputedStyle(r):E.documentElement.currentStyle&&(a=r.currentStyle),(r.offsetWidth<=0&&r.offsetHeight<=0||"hidden"===a.visibility)&&(l=!0),"hidden"!==r.type&&!r.disabled&&!l){r.focus();break}}catch(e){}return!1}}}}(window);
(function($){
jQuery('ul.nd_tabs li:first').addClass('active');
jQuery('form.nd_form, div.nd_logged_in').hide();
jQuery('form.nd_form:first, div.nd_logged_in:first').show();
jQuery('ul.nd_tabs li a:not(ul.nd_tabs li.tab_right a), form.nd_form a.forgotten').click(function(){
jQuery('form.nd_form, div.nd_logged_in').hide();
jQuery('ul.nd_tabs li').removeClass('active');
jQuery(this).parent().addClass('active');
jQuery(jQuery(this).attr('href')).fadeIn();
return false;
});
jQuery('form.nd_form').submit(function(){
var thisform=this;
jQuery('div.nd_form_inner').block({ message: null, overlayCSS: {
backgroundColor: '#fff',
opacity:         0.6 
}});
jQuery.ajax({
type: 'POST',
url: jQuery(thisform).attr('action'),
data: jQuery(thisform).serialize(),
success: function(result){
jQuery('ul.errors, ul.messages').remove();
result=jQuery.trim(result);
if(result=='SUCCESS'){
window.location=jQuery(thisform).attr('action');
}else if(result.substring(8,0)=='SUCCESS:'){
message=result.substr(8);
jQuery('div.nd_form_inner', thisform).prepend('<ul class="messages"><li>' + message + '</li></ul>');
jQuery('div.nd_form_inner').unblock();
}else{
jQuery('div.nd_form_inner', thisform).prepend('<ul class="errors"><li>' + result + '</li></ul>');
jQuery('div.nd_form_inner').unblock();
}}
});
return false;
});
})(jQuery);
;(function(){
"use strict";
function setup($){
$.fn._fadeIn=$.fn.fadeIn;
var noOp=$.noop||function(){};
var msie=/MSIE/.test(navigator.userAgent);
var ie6=/MSIE 6.0/.test(navigator.userAgent)&&! /MSIE 8.0/.test(navigator.userAgent);
var mode=document.documentMode||0;
var setExpr=$.isFunction(document.createElement('div').style.setExpression);
$.blockUI=function(opts){ install(window, opts); };
$.unblockUI=function(opts){ remove(window, opts); };
$.growlUI=function(title, message, timeout, onClose){
var $m=$('<div class="growlUI"></div>');
if(title) $m.append('<h1>'+title+'</h1>');
if(message) $m.append('<h2>'+message+'</h2>');
if(timeout===undefined) timeout=3000;
var callBlock=function(opts){
opts=opts||{};
$.blockUI({
message: $m,
fadeIn:typeof opts.fadeIn!=='undefined' ? opts.fadeIn:700,
fadeOut: typeof opts.fadeOut!=='undefined' ? opts.fadeOut:1000,
timeout: typeof opts.timeout!=='undefined' ? opts.timeout:timeout,
centerY: false,
showOverlay: false,
onUnblock: onClose,
css: $.blockUI.defaults.growlCSS
});
};
callBlock();
var nonmousedOpacity=$m.css('opacity');
$m.mouseover(function(){
callBlock({
fadeIn: 0,
timeout: 30000
});
var displayBlock=$('.blockMsg');
displayBlock.stop();
displayBlock.fadeTo(300, 1);
}).mouseout(function(){
$('.blockMsg').fadeOut(1000);
});
};
$.fn.block=function(opts){
if(this[0]===window){
$.blockUI(opts);
return this;
}
var fullOpts=$.extend({}, $.blockUI.defaults, opts||{});
this.each(function(){
var $el=$(this);
if(fullOpts.ignoreIfBlocked&&$el.data('blockUI.isBlocked'))
return;
$el.unblock({ fadeOut: 0 });
});
return this.each(function(){
if($.css(this,'position')=='static'){
this.style.position='relative';
$(this).data('blockUI.static', true);
}
this.style.zoom=1;
install(this, opts);
});
};
$.fn.unblock=function(opts){
if(this[0]===window){
$.unblockUI(opts);
return this;
}
return this.each(function(){
remove(this, opts);
});
};
$.blockUI.version=2.60;
$.blockUI.defaults={
message:  '<h1>Please wait...</h1>',
title: null,
draggable: true,
theme: false,
css: {
padding:	0,
margin:		0,
width:		'30%',
top:		'40%',
left:		'35%',
textAlign:	'center',
color:		'#000',
border:		'3px solid #aaa',
backgroundColor:'#fff',
cursor:		'wait'
},
themedCSS: {
width:	'30%',
top:	'40%',
left:	'35%'
},
overlayCSS:  {
backgroundColor:	'#000',
opacity:			0.6,
cursor:				'wait'
},
cursorReset: 'default',
growlCSS: {
width:		'350px',
top:		'10px',
left:		'',
right:		'10px',
border:		'none',
padding:	'5px',
opacity:	0.6,
cursor:		'default',
color:		'#fff',
backgroundColor: '#000',
'-webkit-border-radius':'10px',
'-moz-border-radius':	'10px',
'border-radius':		'10px'
},
iframeSrc: /^https/i.test(window.location.href||'') ? 'javascript:false':'about:blank',
forceIframe: false,
baseZ: 1000,
centerX: true,
centerY: true,
allowBodyStretch: true,
bindEvents: true,
constrainTabKey: true,
fadeIn:  200,
fadeOut:  400,
timeout: 0,
showOverlay: true,
focusInput: true,
focusableElements: ':input:enabled:visible',
onBlock: null,
onUnblock: null,
onOverlayClick: null,
quirksmodeOffsetHack: 4,
blockMsgClass: 'blockMsg',
ignoreIfBlocked: false
};
var pageBlock=null;
var pageBlockEls=[];
function install(el, opts){
var css, themedCSS;
var full=(el==window);
var msg=(opts&&opts.message!==undefined ? opts.message:undefined);
opts=$.extend({}, $.blockUI.defaults, opts||{});
if(opts.ignoreIfBlocked&&$(el).data('blockUI.isBlocked'))
return;
opts.overlayCSS=$.extend({}, $.blockUI.defaults.overlayCSS, opts.overlayCSS||{});
css=$.extend({}, $.blockUI.defaults.css, opts.css||{});
if(opts.onOverlayClick)
opts.overlayCSS.cursor='pointer';
themedCSS=$.extend({}, $.blockUI.defaults.themedCSS, opts.themedCSS||{});
msg=msg===undefined ? opts.message:msg;
if(full&&pageBlock)
remove(window, {fadeOut:0});
if(msg&&typeof msg!='string'&&(msg.parentNode||msg.jquery)){
var node=msg.jquery ? msg[0]:msg;
var data={};
$(el).data('blockUI.history', data);
data.el=node;
data.parent=node.parentNode;
data.display=node.style.display;
data.position=node.style.position;
if(data.parent)
data.parent.removeChild(node);
}
$(el).data('blockUI.onUnblock', opts.onUnblock);
var z=opts.baseZ;
var lyr1, lyr2, lyr3, s;
if(msie||opts.forceIframe)
lyr1=$('<iframe class="blockUI" style="z-index:'+ (z++) +';display:none;border:none;margin:0;padding:0;position:absolute;width:100%;height:100%;top:0;left:0" src="'+opts.iframeSrc+'"></iframe>');
else
lyr1=$('<div class="blockUI" style="display:none"></div>');
if(opts.theme)
lyr2=$('<div class="blockUI blockOverlay ui-widget-overlay" style="z-index:'+ (z++) +';display:none"></div>');
else
lyr2=$('<div class="blockUI blockOverlay" style="z-index:'+ (z++) +';display:none;border:none;margin:0;padding:0;width:100%;height:100%;top:0;left:0"></div>');
if(opts.theme&&full){
s='<div class="blockUI ' + opts.blockMsgClass + ' blockPage ui-dialog ui-widget ui-corner-all" style="z-index:'+(z+10)+';display:none;position:fixed">';
if(opts.title){
s +='<div class="ui-widget-header ui-dialog-titlebar ui-corner-all blockTitle">'+(opts.title||'&nbsp;')+'</div>';
}
s +='<div class="ui-widget-content ui-dialog-content"></div>';
s +='</div>';
}
else if(opts.theme){
s='<div class="blockUI ' + opts.blockMsgClass + ' blockElement ui-dialog ui-widget ui-corner-all" style="z-index:'+(z+10)+';display:none;position:absolute">';
if(opts.title){
s +='<div class="ui-widget-header ui-dialog-titlebar ui-corner-all blockTitle">'+(opts.title||'&nbsp;')+'</div>';
}
s +='<div class="ui-widget-content ui-dialog-content"></div>';
s +='</div>';
}
else if(full){
s='<div class="blockUI ' + opts.blockMsgClass + ' blockPage" style="z-index:'+(z+10)+';display:none;position:fixed"></div>';
}else{
s='<div class="blockUI ' + opts.blockMsgClass + ' blockElement" style="z-index:'+(z+10)+';display:none;position:absolute"></div>';
}
lyr3=$(s);
if(msg){
if(opts.theme){
lyr3.css(themedCSS);
lyr3.addClass('ui-widget-content');
}
else
lyr3.css(css);
}
if(!opts.theme )
lyr2.css(opts.overlayCSS);
lyr2.css('position', full ? 'fixed':'absolute');
if(msie||opts.forceIframe)
lyr1.css('opacity',0.0);
var layers=[lyr1,lyr2,lyr3], $par=full ? $('body'):$(el);
$.each(layers, function(){
this.appendTo($par);
});
if(opts.theme&&opts.draggable&&$.fn.draggable){
lyr3.draggable({
handle: '.ui-dialog-titlebar',
cancel: 'li'
});
}
var expr=setExpr&&(!$.support.boxModel||$('object,embed', full ? null:el).length > 0);
if(ie6||expr){
if(full&&opts.allowBodyStretch&&$.support.boxModel)
$('html,body').css('height','100%');
if((ie6||!$.support.boxModel)&&!full){
var t=sz(el,'borderTopWidth'), l=sz(el,'borderLeftWidth');
var fixT=t ? '(0 - '+t+')':0;
var fixL=l ? '(0 - '+l+')':0;
}
$.each(layers, function(i,o){
var s=o[0].style;
s.position='absolute';
if(i < 2){
if(full)
s.setExpression('height','Math.max(document.body.scrollHeight, document.body.offsetHeight) - (jQuery.support.boxModel?0:'+opts.quirksmodeOffsetHack+') + "px"');
else
s.setExpression('height','this.parentNode.offsetHeight + "px"');
if(full)
s.setExpression('width','jQuery.support.boxModel&&document.documentElement.clientWidth||document.body.clientWidth + "px"');
else
s.setExpression('width','this.parentNode.offsetWidth + "px"');
if(fixL) s.setExpression('left', fixL);
if(fixT) s.setExpression('top', fixT);
}
else if(opts.centerY){
if(full) s.setExpression('top','(document.documentElement.clientHeight||document.body.clientHeight) / 2 - (this.offsetHeight / 2) + (blah=document.documentElement.scrollTop ? document.documentElement.scrollTop:document.body.scrollTop) + "px"');
s.marginTop=0;
}
else if(!opts.centerY&&full){
var top=(opts.css&&opts.css.top) ? parseInt(opts.css.top, 10):0;
var expression='((document.documentElement.scrollTop ? document.documentElement.scrollTop:document.body.scrollTop) + '+top+') + "px"';
s.setExpression('top',expression);
}});
}
if(msg){
if(opts.theme)
lyr3.find('.ui-widget-content').append(msg);
else
lyr3.append(msg);
if(msg.jquery||msg.nodeType)
$(msg).show();
}
if((msie||opts.forceIframe)&&opts.showOverlay)
lyr1.show();
if(opts.fadeIn){
var cb=opts.onBlock ? opts.onBlock:noOp;
var cb1=(opts.showOverlay&&!msg) ? cb:noOp;
var cb2=msg ? cb:noOp;
if(opts.showOverlay)
lyr2._fadeIn(opts.fadeIn, cb1);
if(msg)
lyr3._fadeIn(opts.fadeIn, cb2);
}else{
if(opts.showOverlay)
lyr2.show();
if(msg)
lyr3.show();
if(opts.onBlock)
opts.onBlock();
}
bind(1, el, opts);
if(full){
pageBlock=lyr3[0];
pageBlockEls=$(opts.focusableElements,pageBlock);
if(opts.focusInput)
setTimeout(focus, 20);
}
else
center(lyr3[0], opts.centerX, opts.centerY);
if(opts.timeout){
var to=setTimeout(function(){
if(full)
$.unblockUI(opts);
else
$(el).unblock(opts);
}, opts.timeout);
$(el).data('blockUI.timeout', to);
}}
function remove(el, opts){
var count;
var full=(el==window);
var $el=$(el);
var data=$el.data('blockUI.history');
var to=$el.data('blockUI.timeout');
if(to){
clearTimeout(to);
$el.removeData('blockUI.timeout');
}
opts=$.extend({}, $.blockUI.defaults, opts||{});
bind(0, el, opts);
if(opts.onUnblock===null){
opts.onUnblock=$el.data('blockUI.onUnblock');
$el.removeData('blockUI.onUnblock');
}
var els;
if(full)
els=$('body').children().filter('.blockUI').add('body > .blockUI');
else
els=$el.find('>.blockUI');
if(opts.cursorReset){
if(els.length > 1)
els[1].style.cursor=opts.cursorReset;
if(els.length > 2)
els[2].style.cursor=opts.cursorReset;
}
if(full)
pageBlock=pageBlockEls=null;
if(opts.fadeOut){
count=els.length;
els.stop().fadeOut(opts.fadeOut, function(){
if(--count===0)
reset(els,data,opts,el);
});
}
else
reset(els, data, opts, el);
}
function reset(els,data,opts,el){
var $el=$(el);
if($el.data('blockUI.isBlocked'))
return;
els.each(function(i,o){
if(this.parentNode)
this.parentNode.removeChild(this);
});
if(data&&data.el){
data.el.style.display=data.display;
data.el.style.position=data.position;
if(data.parent)
data.parent.appendChild(data.el);
$el.removeData('blockUI.history');
}
if($el.data('blockUI.static')){
$el.css('position', 'static');
}
if(typeof opts.onUnblock=='function')
opts.onUnblock(el,opts);
var body=$(document.body), w=body.width(), cssW=body[0].style.width;
body.width(w-1).width(w);
body[0].style.width=cssW;
}
function bind(b, el, opts){
var full=el==window, $el=$(el);
if(!b&&(full&&!pageBlock||!full&&!$el.data('blockUI.isBlocked')))
return;
$el.data('blockUI.isBlocked', b);
if(!full||!opts.bindEvents||(b&&!opts.showOverlay))
return;
var events='mousedown mouseup keydown keypress keyup touchstart touchend touchmove';
if(b)
$(document).bind(events, opts, handler);
else
$(document).unbind(events, handler);
}
function handler(e){
if(e.type==='keydown'&&e.keyCode&&e.keyCode==9){
if(pageBlock&&e.data.constrainTabKey){
var els=pageBlockEls;
var fwd = !e.shiftKey&&e.target===els[els.length-1];
var back=e.shiftKey&&e.target===els[0];
if(fwd||back){
setTimeout(function(){focus(back);},10);
return false;
}}
}
var opts=e.data;
var target=$(e.target);
if(target.hasClass('blockOverlay')&&opts.onOverlayClick)
opts.onOverlayClick();
if(target.parents('div.' + opts.blockMsgClass).length > 0)
return true;
return target.parents().children().filter('div.blockUI').length===0;
}
function focus(back){
if(!pageBlockEls)
return;
var e=pageBlockEls[back===true ? pageBlockEls.length-1:0];
if(e)
e.focus();
}
function center(el, x, y){
var p=el.parentNode, s=el.style;
var l=((p.offsetWidth - el.offsetWidth)/2) - sz(p,'borderLeftWidth');
var t=((p.offsetHeight - el.offsetHeight)/2) - sz(p,'borderTopWidth');
if(x) s.left=l > 0 ? (l+'px'):'0';
if(y) s.top=t > 0 ? (t+'px'):'0';
}
function sz(el, p){
return parseInt($.css(el,p),10)||0;
}}
if(typeof define==='function'&&define.amd&&define.amd.jQuery){
define(['jquery'], setup);
}else{
setup(jQuery);
}})();
if(!function(t){"use strict";var e=function(t,e){this.init("tooltip",t,e)};e.prototype={constructor:e,init:function(e,i,n){var o,s,r,a,l;for(this.type=e,this.$element=t(i),this.options=this.getOptions(n),this.enabled=!0,r=this.options.trigger.split(" "),l=r.length;l--;)a=r[l],"click"==a?this.$element.on("click."+this.type,this.options.selector,t.proxy(this.toggle,this)):"manual"!=a&&(o="hover"==a?"mouseenter":"focus",s="hover"==a?"mouseleave":"blur",this.$element.on(o+"."+this.type,this.options.selector,t.proxy(this.enter,this)),this.$element.on(s+"."+this.type,this.options.selector,t.proxy(this.leave,this)));this.options.selector?this._options=t.extend({},this.options,{trigger:"manual",selector:""}):this.fixTitle()},getOptions:function(e){return e=t.extend({},t.fn[this.type].defaults,this.$element.data(),e),e.delay&&"number"==typeof e.delay&&(e.delay={show:e.delay,hide:e.delay}),e},enter:function(e){var i,n=t.fn[this.type].defaults,o={};return this._options&&t.each(this._options,function(t,e){n[t]!=e&&(o[t]=e)},this),i=t(e.currentTarget)[this.type](o).data(this.type),i.options.delay&&i.options.delay.show?(clearTimeout(this.timeout),i.hoverState="in",void(this.timeout=setTimeout(function(){"in"==i.hoverState&&i.show()},i.options.delay.show))):i.show()},leave:function(e){var i=t(e.currentTarget)[this.type](this._options).data(this.type);return this.timeout&&clearTimeout(this.timeout),i.options.delay&&i.options.delay.hide?(i.hoverState="out",void(this.timeout=setTimeout(function(){"out"==i.hoverState&&i.hide()},i.options.delay.hide))):i.hide()},show:function(){var e,i,n,o,s,r,a=t.Event("show");if(this.hasContent()&&this.enabled){if(this.$element.trigger(a),a.isDefaultPrevented())return;switch(e=this.tip(),this.setContent(),this.options.animation&&e.addClass("fade"),s="function"==typeof this.options.placement?this.options.placement.call(this,e[0],this.$element[0]):this.options.placement,e.detach().css({top:0,left:0,display:"block"}),this.options.container?e.appendTo(this.options.container):e.insertAfter(this.$element),i=this.getPosition(),n=e[0].offsetWidth,o=e[0].offsetHeight,s){case"bottom":r={top:i.top+i.height,left:i.left+i.width/2-n/2};break;case"top":r={top:i.top-o,left:i.left+i.width/2-n/2};break;case"left":r={top:i.top+i.height/2-o/2,left:i.left-n};break;case"right":r={top:i.top+i.height/2-o/2,left:i.left+i.width}}this.applyPlacement(r,s),this.$element.trigger("shown")}},applyPlacement:function(t,e){var i,n,o,s,r=this.tip(),a=r[0].offsetWidth,l=r[0].offsetHeight;r.offset(t).addClass(e).addClass("in"),i=r[0].offsetWidth,n=r[0].offsetHeight,"top"==e&&n!=l&&(t.top=t.top+l-n,s=!0),"bottom"==e||"top"==e?(o=0,t.left<0&&(o=-2*t.left,t.left=0,r.offset(t),i=r[0].offsetWidth,n=r[0].offsetHeight),this.replaceArrow(o-a+i,i,"left")):this.replaceArrow(n-l,n,"top"),s&&r.offset(t)},replaceArrow:function(t,e,i){this.arrow().css(i,t?50*(1-t/e)+"%":"")},setContent:function(){var t=this.tip(),e=this.getTitle();t.find(".tooltip-inner")[this.options.html?"html":"text"](e),t.removeClass("fade in top bottom left right")},hide:function(){function e(){var e=setTimeout(function(){i.off(t.support.transition.end).detach()},500);i.one(t.support.transition.end,function(){clearTimeout(e),i.detach()})}var i=this.tip(),n=t.Event("hide");return this.$element.trigger(n),n.isDefaultPrevented()?void 0:(i.removeClass("in"),t.support.transition&&this.$tip.hasClass("fade")?e():i.detach(),this.$element.trigger("hidden"),this)},fixTitle:function(){var t=this.$element;(t.attr("title")||"string"!=typeof t.attr("data-original-title"))&&t.attr("data-original-title",t.attr("title")||"").attr("title","")},hasContent:function(){return this.getTitle()},getPosition:function(){var e=this.$element[0];return t.extend({},"function"==typeof e.getBoundingClientRect?e.getBoundingClientRect():{width:e.offsetWidth,height:e.offsetHeight},this.$element.offset())},getTitle:function(){var t,e=this.$element,i=this.options;return t=e.attr("data-original-title")||("function"==typeof i.title?i.title.call(e[0]):i.title)},tip:function(){return this.$tip=this.$tip||t(this.options.template)},arrow:function(){return this.$arrow=this.$arrow||this.tip().find(".tooltip-arrow")},validate:function(){this.$element[0].parentNode||(this.hide(),this.$element=null,this.options=null)},enable:function(){this.enabled=!0},disable:function(){this.enabled=!1},toggleEnabled:function(){this.enabled=!this.enabled},toggle:function(e){var i=e?t(e.currentTarget)[this.type](this._options).data(this.type):this;i.tip().hasClass("in")?i.hide():i.show()},destroy:function(){this.hide().$element.off("."+this.type).removeData(this.type)}};var i=t.fn.tooltip;t.fn.tooltip=function(i){return this.each(function(){var n=t(this),o=n.data("tooltip"),s="object"==typeof i&&i;o||n.data("tooltip",o=new e(this,s)),"string"==typeof i&&o[i]()})},t.fn.tooltip.Constructor=e,t.fn.tooltip.defaults={animation:!0,placement:"top",selector:!1,template:'<div class="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',trigger:"hover focus",title:"",delay:0,html:!1,container:!1},t.fn.tooltip.noConflict=function(){return t.fn.tooltip=i,this}}(window.jQuery),"undefined"==typeof jQuery)throw new Error("WP Ulike's JavaScript requires jQuery");if(+function(t){"use strict";function e(){var t=document.createElement("bootstrap"),e={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var i in e)if(void 0!==t.style[i])return{end:e[i]};return!1}t.fn.emulateTransitionEnd=function(e){var i=!1,n=this;t(this).one("bsTransitionEnd",function(){i=!0});var o=function(){i||t(n).trigger(t.support.transition.end)};return setTimeout(o,e),this},t(function(){t.support.transition=e(),t.support.transition&&(t.event.special.bsTransitionEnd={bindType:t.support.transition.end,delegateType:t.support.transition.end,handle:function(e){return t(e.target).is(this)?e.handleObj.handler.apply(this,arguments):void 0}})})}(jQuery),"undefined"==typeof jQuery)throw new Error("WP Ulike's JavaScript requires jQuery");+function(t){"use strict";function e(e){return this.each(function(){var i=t(this),o=i.data("bs.alert");o||i.data("bs.alert",o=new n(this)),"string"==typeof e&&o[e].call(i)})}var i='[data-dismiss="alert"]',n=function(e){t(e).on("click",i,this.close)};n.VERSION="3.2.0",n.prototype.close=function(e){function i(){s.detach().trigger("closed.bs.alert").remove()}var n=t(this),o=n.attr("data-target");o||(o=n.attr("href"),o=o&&o.replace(/.*(?=#[^\s]*$)/,""));var s=t(o);e&&e.preventDefault(),s.length||(s=n.hasClass("alert")?n:n.parent()),s.trigger(e=t.Event("close.bs.alert")),e.isDefaultPrevented()||(s.removeClass("in"),t.support.transition&&s.hasClass("fade")?s.one("bsTransitionEnd",i).emulateTransitionEnd(150):i())};var o=t.fn.alert;t.fn.alert=e,t.fn.alert.Constructor=n,t.fn.alert.noConflict=function(){return t.fn.alert=o,this},t(document).on("click.bs.alert.data-api",i,n.prototype.close)}(jQuery),jQuery(document).ready(function(t){t(".user-tooltip").tooltip()});