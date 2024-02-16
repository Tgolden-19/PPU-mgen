"""
test module for txtmsggen.py functions to ensure they work
Created by Tristan Golden on 9/7/20
"""

from txtmsggen import *

# below is the html for the unit test
html = """
<!DOCTYPE html>
<!--[if IE 8]> <html lang="en" class="ie8 no-js"> <![endif]-->
<!--[if IE 9]> <html lang="en" class="ie9 no-js"> <![endif]-->
<!--[if !IE]><!-->
<html lang="en">
    <!--<![endif]-->
    <head>

        <meta charset="utf-8" />
        <title>Point Pickup - CONTROL PANEL - Deliveries Info Pk-8293046586 As-it-is</title>

        <meta http-equiv="X-UA-Compatible" content="IE=edge"><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:true}};(window.NREUM||(NREUM={})).loader_config={licenseKey:"NRJS-aeb285a862dbe7cc429",applicationID:"712421119"};window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var i=n[t]={exports:{}};e[t][0].call(i.exports,function(n){var i=e[t][1][n];return r(i||n)},i,i.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<t.length;i++)r(t[i]);return r}({1:[function(e,n,t){function r(){}function i(e,n,t){return function(){return o(e,[u.now()].concat(c(arguments)),n?null:this,t),n?void 0:this}}var o=e("handle"),a=e(5),c=e(6),f=e("ee").get("tracer"),u=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(e,n){s[n]=i(p+n,!0,"api")}),s.addPageAction=i(p+"addPageAction",!0),s.setCurrentRouteName=i(p+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,i="function"==typeof n;return o(l+"tracer",[u.now(),e,t],r),function(){if(f.emit((i?"":"no-")+"fn-start",[u.now(),r,i],t),i)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[u.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=i(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),o("err",[e,u.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){var t=e.getEntries();t.forEach(function(e){"first-paint"===e.name?d("timing",["fp",Math.floor(e.startTime)]):"first-contentful-paint"===e.name&&d("timing",["fcp",Math.floor(e.startTime)])})}function i(e,n){var t=e.getEntries();t.length>0&&d("lcp",[t[t.length-1]])}function o(e){e.getEntries().forEach(function(e){e.hadRecentInput||d("cls",[e])})}function a(e){if(e instanceof m&&!g){var n=Math.round(e.timeStamp),t={type:e.type};n<=p.now()?t.fid=p.now()-n:n>p.offset&&n<=Date.now()?(n-=p.offset,t.fid=p.now()-n):n=p.now(),g=!0,d("timing",["fi",n,t])}}function c(e){d("pageHide",[p.now(),e])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var f,u,s,d=e("handle"),p=e("loader"),l=e(4),m=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){f=new PerformanceObserver(r);try{f.observe({entryTypes:["paint"]})}catch(v){}u=new PerformanceObserver(i);try{u.observe({entryTypes:["largest-contentful-paint"]})}catch(v){}s=new PerformanceObserver(o);try{s.observe({type:"layout-shift",buffered:!0})}catch(v){}}if("addEventListener"in document){var g=!1,y=["click","keydown","mousedown","pointerdown","touchstart"];y.forEach(function(e){document.addEventListener(e,a,!1)})}l(c)}},{}],3:[function(e,n,t){function r(e,n){if(!i)return!1;if(e!==i)return!1;if(!n)return!0;if(!o)return!1;for(var t=o.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var c=navigator.userAgent,f=c.match(a);f&&c.indexOf("Chrome")===-1&&c.indexOf("Chromium")===-1&&(i="Safari",o=f[1])}n.exports={agent:i,version:o,match:r}},{}],4:[function(e,n,t){function r(e){function n(){e(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,n,!1)}n.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],5:[function(e,n,t){function r(e,n){var t=[],r="",o=0;for(r in e)i.call(e,r)&&(t[o]=n(r,e[r]),o+=1);return t}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],6:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,i=t-n||0,o=Array(i<0?0:i);++r<i;)o[r]=e[n+r];return o}n.exports=r},{}],7:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function i(e){function n(e){return e&&e instanceof r?e:e?f(e,c,o):o()}function t(t,r,i,o){if(!p.aborted||o){e&&e(t,r,i);for(var a=n(i),c=v(t),f=c.length,u=0;u<f;u++)c[u].apply(a,r);var d=s[w[t]];return d&&d.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return d[e]=d[e]||i(t)}function y(e,n){u(e,function(e,t){n=n||"feature",w[t]=n,n in s||(s[n]=[])})}var h={},w={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:y,abort:a,aborted:!1};return b}function o(){return new r}function a(){(s.api||s.feature)&&(p.aborted=!0,s=p.backlog={})}var c="nr@context",f=e("gos"),u=e(5),s={},d={},p=n.exports=i();p.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(i.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return e[n]=r,r}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){i.buffer([e],r),i.emit(e,n,t)}var i=e("ee").get("handle");n.exports=r,r.ee=i},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,o,function(){return i++})}var i=1,o="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=E.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();u(w,function(n,t){e[n]||(e[n]=t)});var t=a();f("mark",["onload",t+E.offset],null,"api"),f("timing",["load",t]);var r=l.createElement("script");r.src="https://"+e.agent,n.parentNode.insertBefore(r,n)}}function i(){"complete"===l.readyState&&o()}function o(){f("mark",["domContent",a()+E.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(c=Math.max((new Date).getTime(),c))-E.offset}var c=(new Date).getTime(),f=e("handle"),u=e(5),s=e("ee"),d=e(3),p=window,l=p.document,m="addEventListener",v="attachEvent",g=p.XMLHttpRequest,y=g&&g.prototype;NREUM.o={ST:setTimeout,SI:p.setImmediate,CT:clearTimeout,XHR:g,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var h=""+location,w={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1177.min.js"},b=g&&y&&y[m]&&!/CriOS/.test(navigator.userAgent),E=n.exports={offset:c,now:a,origin:h,features:{},xhrWrappable:b,userAgent:d};e(1),e(2),l[m]?(l[m]("DOMContentLoaded",o,!1),p[m]("load",r,!1)):(l[v]("onreadystatechange",i),p[v]("onload",r)),f("mark",["firstbyte",c],null,"api");var x=0,O=e(7)},{}],"wrap-function":[function(e,n,t){function r(e){return!(e&&e instanceof Function&&e.apply&&!e[a])}var i=e("ee"),o=e(6),a="nr@original",c=Object.prototype.hasOwnProperty,f=!1;n.exports=function(e,n){function t(e,n,t,i){function nrWrapper(){var r,a,c,f;try{a=this,r=o(arguments),c="function"==typeof t?t(r,a):t||{}}catch(u){p([u,"",[r,a,i],c])}s(n+"start",[r,a,i],c);try{return f=e.apply(a,r)}catch(d){throw s(n+"err",[r,a,d],c),d}finally{s(n+"end",[r,a,f],c)}}return r(e)?e:(n||(n=""),nrWrapper[a]=e,d(e,nrWrapper),nrWrapper)}function u(e,n,i,o){i||(i="");var a,c,f,u="-"===i.charAt(0);for(f=0;f<n.length;f++)c=n[f],a=e[c],r(a)||(e[c]=t(a,u?c+i:i,o,c))}function s(t,r,i){if(!f||n){var o=f;f=!0;try{e.emit(t,r,i,n)}catch(a){p([a,t,r,i])}f=o}}function d(e,n){if(Object.defineProperty&&Object.keys)try{var t=Object.keys(e);return t.forEach(function(t){Object.defineProperty(n,t,{get:function(){return e[t]},set:function(n){return e[t]=n,n}})}),n}catch(r){p([r])}for(var i in e)c.call(e,i)&&(n[i]=e[i]);return n}function p(n){try{e.emit("internal-error",n)}catch(t){}}return e||(e=i),t.inPlace=u,t.flag=a,t}},{}]},{},["loader"]);</script>
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <base href="https://pointpickup.com/" >

        <link href="//fonts.googleapis.com/css?family=Open+Sans:400,300,600,700&subset=all" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/plugins/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/plugins/bootstrap-switch/css/bootstrap-switch.min.css" rel="stylesheet" type="text/css" />

        <link href="https://pointpickup.com/assets/control-panel/plugins/select2/css/select2.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/plugins/select2/css/select2-bootstrap.min.css" rel="stylesheet" type="text/css" />

        <link href="https://pointpickup.com/assets/control-panel/css/components.min.css" rel="stylesheet" id="style_components" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/css/plugins.min.css" rel="stylesheet" type="text/css" />

        <link href="https://pointpickup.com/assets/control-panel/layout/css/layout.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/layout/css/themes/darkblue.min.css" rel="stylesheet" type="text/css" id="style_color" />
        <link href="https://pointpickup.com/assets/control-panel/layout/css/custom.min.css" rel="stylesheet" type="text/css" />

        <link href="https://pointpickup.com/assets/control-panel/plugins/bootstrap-daterangepicker/daterangepicker.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/css/flatpickr.min.css" rel="stylesheet" type="text/css" />

        <link href="https://pointpickup.com/assets/control-panel/pages/css/profile.min.css" rel="stylesheet" type="text/css" />
        <link href="https://pointpickup.com/assets/control-panel/css/main.css?v=2020090722" rel="stylesheet" type="text/css" />

        <script src="//browser.sentry-cdn.com/5.15.5/bundle.min.js" integrity="sha384-wF7Jc4ZlWVxe/L8Ji3hOIBeTgo/HwFuaeEfjGmS3EXAG7Y+7Kjjr91gJpJtr+PAT" crossorigin="anonymous"></script>
        <script> Sentry.init({ dsn: "https://5d77be431ccf4e059adb0f55919d6a6a@sentry.prod.ppup.io/3" }); </script>
    </head>

</head>
<body id="deliveries-infomultiple" class="page-header-fixed page-sidebar-closed-hide-logo page-container-bg-solid page-content-white">
    <div class="page-wrapper">

        <!-- BEGIN HEADER -->
        <div class="page-header navbar navbar-fixed-top">
            <div class="page-header-inner ">
                <div class="page-logo">
                    <a href="https://pointpickup.com/control-panel/">
                        <img src="https://pointpickup.com/assets/control-panel/img/logo.svg" alt="logo" class="logo-default" /> </a>
                    <div class="menu-toggler sidebar-toggler">
                        <span></span>
                    </div>
                </div>
                <a href="javascript:;" class="menu-toggler responsive-toggler" data-toggle="collapse" data-target=".navbar-collapse">
                    <span></span>
                </a>
                <div class="top-menu">
                    <ul class="nav navbar-nav pull-right">
                        <li class="dropdown dropdown-extended dropdown-notification" id="header_notification_bar">
                            <a href="https://pointpickup.com/control-panel/notifications" class="dropdown-toggle" >
                                <i class="icon-bell"></i>
                                <span class="badge badge-default" id="notification-nbadge"
                                    data-uid="237"
                                    data-src="https://pointpickup.com/control-panel/notifications/notification_badge"
                                >
                                    0
                                </span>
                            </a>
                        </li>

                        <li class="dropdown dropdown-user">
                            <a href="javascript:;" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" data-close-others="true">
                                <span class="username username-hide-on-mobile"> Tristan Golden </span>
                                <i class="fa fa-angle-down"></i>
                            </a>
                            <ul class="dropdown-menu dropdown-menu-default">
                                <li>
                                    <a href="https://pointpickup.com/control-panel/my-account">
                                        <i class="icon-user"></i>
                                        My Profile
                                    </a>
                                </li>
                                <li class="divider"> </li>
                                <li>
                                    <a href="https://pointpickup.com/control-panel/lockscreen">
                                        <i class="icon-lock"></i>
                                        Lock Screen
                                    </a>
                                </li>
                                <li>
                                    <a href="https://pointpickup.com/control-panel/logout">
                                        <i class="icon-key"></i>
                                        Log Out
                                    </a>
                                </li>
                            </ul>
                        </li>
                        <li class="dropdown dropdown-quick-sidebar-toggler">
                            <a href="https://pointpickup.com/control-panel/logout" class="dropdown-toggle">
                                <i class="icon-logout"></i>
                            </a>
                        </li>

                    </ul>
                </div>
            </div>
        </div>
        <!-- END HEADER -->

        <!-- BEGIN HEADER & CONTENT DIVIDER -->
        <div class="clearfix"> </div>
        <!-- END HEADER & CONTENT DIVIDER -->

        <!-- BEGIN CONTAINER -->
        <div class="page-container">

            <!-- BEGIN SIDEBAR -->
            <div class="page-sidebar-wrapper">

                <div class="page-sidebar navbar-collapse collapse">
                    <ul class="page-sidebar-menu  page-header-fixed " data-keep-expanded="false" data-auto-scroll="true" data-slide-speed="200" style="padding-top: 20px">
                        <!-- BEGIN SIDEBAR TOGGLER BUTTON -->
                        <li class="sidebar-toggler-wrapper hide">
                            <div class="sidebar-toggler">
                                <span></span>
                            </div>
                        </li>

                        <li class="heading">
                            <h3 class="uppercase">Main menu</h3>
                        </li>



                                                                <li class="nav-item start ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/dashboard" class="nav-link " data-ss='{"name":"Dashboard","icon":"icon-graph"}'>
                                            <i class="icon-graph"></i>
                                            <span class="title">Dashboard</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/admins" class="nav-link " data-ss='{"name":"Administrators","icon":"icon-user"}'>
                                            <i class="icon-user"></i>
                                            <span class="title">Administrators</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/settings" class="nav-link " data-ss='{"name":"Settings","icon":"fa fa-gear"}'>
                                            <i class="fa fa-gear"></i>
                                            <span class="title">Settings</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>

                                                                    <li class="heading"><!-- separator --></li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/accounts" class="nav-link " data-ss='{"name":"Accounts","icon":"icon-user"}'>
                                            <i class="icon-user"></i>
                                            <span class="title">Accounts</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/deliveries" class="nav-link " data-ss='{"name":"Orders (Deliveries)","icon":"fa fa-car"}'>
                                            <i class="fa fa-car"></i>
                                            <span class="title">Orders (Deliveries)</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/overdue" class="nav-link " data-ss='{"name":"Upcoming & Overdue","icon":"fa fa-clock-o"}'>
                                            <i class="fa fa-clock-o"></i>
                                            <span class="title">Upcoming & Overdue</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>

                                                                    <li class="heading"><!-- separator --></li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/payments" class="nav-link " data-ss='{"name":"Payments","icon":"fa dolar-sign"}'>
                                            <i class="fa dolar-sign"></i>
                                            <span class="title">Payments</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>

                                                                    <li class="heading"><!-- separator --></li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/reports" class="nav-link " data-ss='{"name":"Reports","icon":"fa fa-line-chart"}'>
                                            <i class="fa fa-line-chart"></i>
                                            <span class="title">Reports</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>


                                                                <li class="nav-item  ">


                                        <!--menu entry-->
                                        <a href="https://pointpickup.com/control-panel/app_logs/geofence_log" class="nav-link " data-ss='{"name":"Logs","icon":"fa fa-clock-o"}'>
                                            <i class="fa fa-clock-o"></i>
                                            <span class="title">Logs</span>
                                                                                    </a>
                                        <!--& menu entry-->


                                </li>

                    </ul>
                </div>
            </div>
            <!-- END SIDEBAR -->

            <!-- BEGIN CONTENT -->
            <div class="page-content-wrapper">
                <!-- BEGIN CONTENT BODY -->
                <div class="page-content">


                        <div id="content-notifications">







                        </div>
                        <div id="content">
                            <div class=""><span class="_admin_datetime">Sep 07, 2020 22:21<span></div>
<div>
</div>
<div class="m-grid">
    <div class="m-grid-row">
        <div class="m-grid-col m-grid-col-middle m-grid-col-md-6">

            <!-- BEGIN PAGE TITLE-->
            <h1 class="page-title ">
                                    <div id="route_id_3447323" class="route_id hide show-inline">
                        <i class="fa fa-archive"></i>
                        <p>Order Number:
                            <span style="color:#FF8B00">PK-8293046586-3447323</span>
                            <span class="overdue_asap overdue_asap-labelInfo" style="">ASAP</span>
                            <span class="overdue_asap overdue_asap-labelInfo" style="display: inline-block">Express delivery</span>
                            <span class="route_id-status">Active</span>
                        </p>
                    </div>
                            </h1>
            <!-- END PAGE TITLE-->
            <h5>
                                    B2B Referrer ID: <strong><a href="javascript:;" onclick="ajaxSearchforReferrerID('7522201289280', '2020-09-04 18:41:16', '2020-09-10 18:41:16')">7522201289280</a></strong>
                                                    <span>&nbsp;&nbsp; | &nbsp;&nbsp;</span>
                                                    B2B Child Referrer ID: <strong><a href="javascript:;" onclick="ajaxSearchforChildReferrerID('7522201289280', '2020-09-04 18:41:16', '2020-09-10 18:41:16')">7522201289280</a></strong>
                                                                                    <span>&nbsp;&nbsp; | &nbsp;&nbsp;</span>
                                                    Location code: <strong>WMT5105</strong>
                            </h5>

        </div>

        <div class="m-grid-col m-grid-col-middle m-grid-col-md-4 ">
            <div class="row">
                <div class="col-xs-6 col-xs-offset-1 text-right">
                                                                            </div>
                            </div>
        </div>

        <div class="m-grid-col m-grid-col-middle m-grid-col-md-2 page-bar-container ">

                            <div class="unassignButtonHolder">
                    <a href="javascript:void()" id="manual-remove-driver-3447323" class="btn btn-danger pull-right unassignButton">Remove Driver</a>
                    <br><br><br>
                </div>

                                                                        <div class="geofenceButtonHolder">
                            <a href="https://pointpickup.com/control-panel/deliveries/change_geofence/3447323/disable" class="btn green pull-right geofenceButton">Disable Geofence</a>
                            <br><br><br>
                        </div>

            <div class="notifyDriversHolder">
                <a href="#" class="btn green pull-right notifyDrivers">Notify drivers</a>
                <br><br><br>
            </div>


                                    <div class="diablePhotoProofButtonHolder">
                            <a href="https://pointpickup.com/control-panel/deliveries/disablePhotoProof/3447323/3046586/3474850" class="btn green pull-right disablePhotoProofButton">Disable Photo Proof</a>
                            <br><br><br>
                        </div>

            <!-- BEGIN PAGE BAR -->
            <div class="page-bar">
                <div class="page-toolbar">
                    <div class="btn-group pull-right">
                        <a href='https://pointpickup.com/control-panel/deliveries#delivered' class="cbtn btn green btn-sm btn-outline" >
                            Back
                        </a>

                        <a class="cbtn btn green btn-sm btn-outline" id="loginas" href="https://pointpickup.com/control-panel/deliveries/loginas/PK-8293046586/multiple/as-it-is/3447323" target="_blank">
                            Login As
                        </a>

                                                                                    <a
                                                                    class="cbtn adminDeliver"
                                    data-routeid="3447323"
                                    href=""
                                    >
                                    <button type="button" class="btn green btn-sm btn-outline">
                                        Mark delivered
                                    </button>
                                </a>

                                                    <form action="https://pointpickup.com/control-panel/deliveries/info/PK-8293046586/as-it-is/3447323" method="post" accept-charset="utf-8">


                            <!---<button class="btn green btn-sm btn-outline" type="submit" name="order_cancel">Cancel Order</button>--->


<input type="hidden" name="order-action" value="1" />
                            </form>
                    </div>
                </div>
            </div>
            <!-- END PAGE BAR -->
            <div class="coords-status-led-order">
                <p>
                    <?xml version="1.0" encoding="UTF-8"?>
<svg width="448px" height="321px" viewBox="0 0 448 321" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <!-- Generator: Sketch 57.1 (83088) - https://sketch.com -->
    <title>Untitled</title>
    <desc>Created with Sketch.</desc>
    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="radio-waves" fill="#000000">
            <g id="Group">
                <circle id="Oval" cx="224" cy="160" r="64"></circle>
                <g id="Shape">
                    <path d="M112,160 C112,123.1 130.553,90.792 158.314,72.966 L135.173,48.454 C128.913,53.062 122.993,58.287 117.489,64.117 C93.314,89.729 80,123.781 80,160 C80,196.219 93.314,230.271 117.49,255.883 C122.994,261.712 128.914,266.938 135.174,271.545 L158.315,247.034 C130.553,229.208 112,196.9 112,160 L112,160 Z"></path>
                    <path d="M336,160 C336,196.9 317.447,229.208 289.686,247.034 L312.827,271.545 C319.087,266.938 325.007,261.712 330.511,255.883 C354.686,230.271 368,196.219 368,160 C368,123.781 354.686,89.729 330.51,64.118 C325.006,58.288 319.086,53.063 312.826,48.455 L289.685,72.967 C317.447,90.792 336,123.1 336,160 L336,160 Z"></path>
                    <path d="M32,160 C32,104.422 57.251,55.093 96.263,24.183 L73.433,0 C67.434,5 61.694,10.396 56.236,16.178 C38.614,34.847 24.774,56.595 15.102,80.819 C5.081,105.917 0,132.556 0,160 C0,187.443 5.081,214.084 15.102,239.181 C24.774,263.407 38.614,285.154 56.236,303.823 C61.694,309.604 67.434,315 73.433,320.001 L96.262,295.818 C57.251,264.907 32,215.578 32,160 L32,160 Z"></path>
                    <path d="M416,160 C416,215.578 390.749,264.907 351.738,295.817 L374.566,319.665 C380.566,314.664 386.306,309.603 391.764,303.822 C409.386,285.153 423.226,263.406 432.898,239.18 C442.918,214.084 448,187.443 448,160 C448,132.556 442.918,105.917 432.898,80.819 C423.226,56.594 409.386,34.847 391.764,16.178 C386.307,10.396 380.566,5 374.566,0 L351.737,24.183 C390.749,55.093 416,104.422 416,160 L416,160 Z"></path>
                </g>
            </g>
        </g>
    </g>
</svg><span class="inner-text">Waiting for coordinates</span>                </p>
            </div>
        </div>
    </div>
</div>




<div class="row">
    <div class="col-lg-12">
        <div class="portlet light ">
                            <div id="map_route_3447323" class="map_container hide show" attr-get-status="ORDER_ACTIVE">
                                    </div>
                                        <div class="map-canvas hidden">
                    <div class="map" id="map_routing_hours"></div>
                    <a class="plus"><i class="fa fa-plus"></i></a>
                </div>
                    </div>
    </div>
</div>

<div class="row">
    <div class="col-lg-12">
        <div class="portlet light ">
            <div class="portlet-body">
                                    <div id="timeline_3447323" class="table-holder-tactivity_timeline timeline_wrapper hide show" data-oid="PK-8293046586" data-routeid='3447323' data-webhooks_url='https://developer.api.walmart.com/api-proxy/service/lastmile-webhook/pointpickup/v1/api/webhook/pointpickup'></div>
                            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-lg-12">
        <div class="portlet light ">
            <div class="portlet-body ">
                <div class="tabbable-line">

                    <ul class="nav nav-tabs ">
                                                    <li class="active">
                                <a href="#tab_route_1"
                                   class="route_tab change_route_tab"
                                   data-toggle="tab"
                                   data-routeid="3447323"
                                   >
                                    Route 1 Location
                                </a>
                            </li>

                    </ul>
                    <div class="tab-content">

                                                    <div id="tab_route_1" class="tab-pane active" >
                                <div class="row">
                                    <div class="col-xs-12 text-right">
                                                                                    <div class="buttonDetails_arrow"><i>&nbsp;</i></div>
                                                                            </div>
                                </div>

                                <div class="row" id="route_details_big_3447323" style="display:none;">
                                                                                                                    <div class="col-xs-12">
                                            <div class="point-name">
                                                <h4>
                                                    <!-- <img src="https://pointpickup.com/assets/gateway/img/icons/stop_1.png"> -->
                                                    <span class="number_bullet">1</span>
                                                    <span>Pickup</span>
                                                </h4>
                                                <div class="clearfix"></div>
                                            </div>

                                            <div class="point-details ">
                                                <div class="row">
                                                    <div class="col-xs-6">
                                                        <div class="point-address">
                                                            <h5>10 Riverton Commons Dr, Front Royal, VA, US</h5>
                                                            Business Name:  WalmartStore:5105 <br />
                                                        </div>
                                                    </div>

                                                    <div class="col-xs-6">
                                                        <div class="point_labels_wrapper">
                                                            <div class="point-date">
                                                                Mon, Sep 07, 2020, 06:41 PM (UTC -4.0)                                                            </div>
                                                                                                                                                                                                                                            </div>
                                                    </div>
                                                </div><!-- /.row -->
                                            </div><!-- /.point-details -->
                                                                                            <div class="point-details ">
                                                    <div class="row">
                                                        <div class="col-xs-12">
                                                            <label rel="note-expand">Note <i class="arrow-down noteButton"></i></label>
                                                            <div class="noteHide">
                                                                Express Order (FRONT DOOR entrance): Enter store from main parking lot (MASK REQUIRED). Skip lines by showing driver app. Pick up area is located inside front of store. Look for blue sign EXPRESS DELIVERY DRIVERS PICK UP HERE. Confirm order number. Returns: Go to Pickup parking bays. If none exist, follow in-store pickup instructions above.                                                            </div>
                                                        </div>
                                                    </div><!-- /.row -->
                                                </div><!-- /.point-details -->
                                                                                    </div><!-- /.col-xs-12 -->

                                                                                                                        <div class="col-xs-12">
                                            <div class="point-name">
                                                <h4>
                                                    <!-- <img src="https://pointpickup.com/assets/gateway/img/icons/stop_2.png"> -->
                                                    <span class="number_bullet">2</span>
                                                    <span>Drop-Off</span>
                                                </h4>
                                                <div class="clearfix"></div>
                                            </div>

                                            <div class="point-details noBorder">
                                                <div class="row">
                                                    <div class="col-xs-6">
                                                        <div class="point-address">
                                                            <h5>301 N Fork Rd, Front Royal, VA, USA</h5>
                                                            Apartment Number: 301 N Fork Rd,Front Royal,VA,USA,22630 <br />
                                                        </div>
                                                    </div>

                                                    <div class="col-xs-6">
                                                        <div class="point_labels_wrapper">
                                                            <div class="point-date">
                                                                Mon, Sep 07, 2020, 07:05 PM (UTC -4.0)                                                            </div>
                                                                                                                                                                                                                                            </div>
                                                    </div>
                                                </div><!-- /.row -->
                                            </div><!-- /.point-details -->
                                                                                            <div class="point-details noBorder">
                                                    <div class="row">
                                                        <div class="col-xs-12">
                                                            <label rel="note-expand">Note <i class="arrow-down noteButton"></i></label>
                                                            <div class="noteHide">
                                                                No-contact delivery; customer expectations: (1) carefully place bags at doorstep (2) ring doorbell or knock (3) return to car before door opens (4) line across customer signature screen to complete, where applicable. When you get to the guard shack pull into spots on the left side and notify me when you get here. We must meet you at the parking spots.                                                            </div>
                                                        </div>
                                                    </div><!-- /.row -->
                                                </div><!-- /.point-details -->
                                                                                    </div><!-- /.col-xs-12 -->

                                                                        </div>
                                <div id="route_details_small_3447323">


                                    <div class="point-name">
                                        <h4>
                                            <!-- <img src="https://pointpickup.com/assets/gateway/img/icons/stop_1.png"> -->
                                            <span class="number_bullet">1</span>
                                            <span>Pickup</span>
                                        </h4>
                                    </div>
                                    <div class="point-details">
                                        <div class="row">
                                            <div class="col-xs-6">
                                                <div class="point-address">
                                                    <h5>10 Riverton Commons Dr, Front Royal, VA, US</h5>
                                                    Business Name:  WalmartStore:5105<br />
                                                </div>
                                                <div class="point-notes">
                                                                                                            <p>Express Order (FRONT DOOR entrance): Enter store from main parking lot (MASK REQUIRED). Skip lines by showing driver app. Pick up area is located inside front of store. Look for blue sign EXPRESS DELIVERY DRIVERS PICK UP HERE. Confirm order number. Returns: Go to Pickup parking bays. If none exist, follow in-store pickup instructions above.</p>
                                                                                                    </div>

                                                <div>
                                                    <p></p>
                                                </div>
                                                <div class="point-requirements">
                                                        <p class="title">Order
                                                            Requirements: <span style="color: black; font-weight: normal">
                                                                </span></p>
                                                                                                                                                                                                                <span class="item">In-Store Pickup</span>                                                                                                    </div>
                                            </div>
                                            <div class="col-xs-6">
                                                <div class="point_labels_wrapper">
                                                    <div class="point-date">
                                                        Mon, Sep 07, 2020, 06:41 PM (UTC -4.0)
                                                                                                                    <div class="point-asap">
                                                                <span>ASAP</span>
                                                            </div>
                                                                                                            </div>
                                                                                                    </div>
                                            </div>
                                        </div>
                                    </div>


                                    <div class="point-name">
                                        <h4>
                                            <!-- <img src="https://pointpickup.com/assets/gateway/img/icons/stop_2.png"> -->
                                            <span class="number_bullet">2</span>
                                            <span>Drop-Off</span>
                                        </h4>
                                    </div>
                                    <div class="point-details noBorder">
                                        <div class="row">
                                            <div class="col-xs-6">
                                                <div class="point-address">
                                                    <h5>301 N Fork Rd, Front Royal, VA, USA</h5>
                                                    Apartment Number: 301 N Fork Rd,Front Royal,VA,USA,22630<br />
                                                </div>
                                                <div class="point-notes">
                                                                                                            <p>No-contact delivery; customer expectations: (1) carefully place bags at doorstep (2) ring doorbell or knock (3) return to car before door opens (4) line across customer signature screen to complete, where applicable. When you get to the guard shack pull into spots on the left side and notify me when you get here. We must meet you at the parking spots.</p>
                                                                                                    </div>
                                                                                                <div>
                                                    <p></p>
                                                </div>
                                                <div class="point-requirements">
                                                        <p class="title">Order
                                                            Requirements: <span style="color: black; font-weight: normal"></span></p>

                                                                                                                                                                                                                                                                                                                                                                                        Photo Proof of Delivery
                                                                                                                                                            </div>
                                            </div>
                                            <div class="col-xs-6">
                                                <div class="point_labels_wrapper">
                                                    <div class="point-date">
                                                        Mon, Sep 07, 2020, 07:05 PM (UTC -4.0)                                                                                                                    <div class="point-asap">
                                                                <span>ASAP</span>
                                                            </div>
                                                                                                            </div>
                                                                                                                                                        </div>
                                            </div>
                                        </div>
                                    </div>

                                </div>


                                <div class="mt20 mb20">
                                    <hr/>
                                </div>

                                <div class="row">

                                    <div class="col-md-6">
                                        <div class="col-md-2">
                                            <div class="profile-userpic small">
                                                <img src="https://pointpickup.com/picture/account.png" width="60px" height="60px" alt="">
                                            </div>
                                        </div>
                                        <div class="col-md-10">
                                            <h4>Client</h4>
                                                                                        Account ID: <a href="https://pointpickup.com/control-panel/accounts/info/16862">16862</a><br>
                                            Business name: Walmart Inc.<br>
                                            Full name: <a href="https://pointpickup.com/control-panel/accounts/info/16862">Walmart Inc.</a><br>
                                            Email: <a href="https://pointpickup.com/control-panel/accounts/info/16862">mcho@walmart.com</a><br>
                                            Phone: 1-800-925-6278<br><br>
                                                                                    </div>
                                    </div>

                                    <div class="col-md-6">
                                                                                    <div class="row">
                                                <div class="col-md-2">
                                                    <div class="profile-userpic small">
                                                        <img src="https://pointpickup.com/picture/123203_dd45045f8c68db9f54e70c67048d32e8.png" width="60px" height="60px">
                                                    </div>
                                                </div>
                                                <div class="col-md-10">
                                                    <h4>Pickup Partner</h4>


                                                    Account ID <a href="https://pointpickup.com/control-panel/accounts/info/123203">123203</a><br>
                                                    Full name <a href="https://pointpickup.com/control-panel/accounts/info/123203">Richard Prendergast</a><br>
                                                    Email <a href="https://pointpickup.com/control-panel/accounts/info/123203">prendergast.r@gmail.com</a><br>
                                                    Account role Pickup Partner<br>
                                                    Phone 0012025946931<br>

                                                    <div>
                                                        <div class="stars ">
                                                            <i class="fa fa-star"></i><i class="fa fa-star-o"></i><i class="fa fa-star-o"></i><i class="fa fa-star-o"></i><i class="fa fa-star-o"></i>                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                                                            </div>
                                </div>

                                <div class="mt20 mb20">
                                    <hr/>
                                </div>

                                <div class="table-scrollable table-scrollable-borderless">
                                    <table class="table table-hover table-light">
                                        <tbody>
                                            <tr>
                                                <td><strong>Status</strong></td>
                                                <td>Active</td>
                                            </tr>
                                                                                        <tr>
                                                <td><strong>Publish date</strong></td>
                                                <td><span class="_admin_datetime">Sep 07, 2020 10:21 PM<span></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="mt20 mb20">
                                    <hr/>
                                </div>
                                                                <div class="row ord-details">
                                    <div class="col-xs-12">
                                        <div class="portlet light ">
                                            <div class="portlet-body ">


                                                    <div class="row route-price-details " id="route_price_3447323">
                                                        <div class="col-xs-12" id="route_driver_3447323">

                                                            <div class="ord-details-table-head">
                                                                <div class="item">
                                                                    Order Details and Specific Driver’s Match                                                                </div>
                                                                <div class="item">
                                                                    Fee Breakdown                                                                </div>
                                                            </div>

                                                            <div class="order_details_table">
                                                                <div class="col-sm-6">
                                                                    <div class="ord-details-table-left">
                                                                        <div class="ord-col-1">Distance</div>
                                                                        <div class="ord-col-2">4.80 miles</div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="The base number of miles for this trip">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-table-left">
                                                                        <div class="ord-col-1">Time to complete</div>
                                                                        <div class="ord-col-2">
                                                                                                                                                        00:24:05 min                                                                        </div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="The amount of time before the package must be delivered ">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-table-left">
                                                                        <div class="ord-col-1">Package type</div>
                                                                        <div class="ord-col-2">
                                                                            Groceries                                                                        </div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="The type of package desired to be transported">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-table-left">
                                                                        <div class="ord-col-1">Over 4ft.x4ft</div>
                                                                        <div class="ord-col-2">
                                                                            No                                                                        </div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="If the package is greater than 4ft x 4ft, a 50% oversize fee is charged">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-table-left">
                                                                        <div class="ord-col-1">Additional Settings</div>
                                                                        <div class="ord-col-2"></div>
                                                                        <div class="ord-col-3">
                                                                            <div class="orderSlideDown butonDetaliiComanda" data-type="ord-details-preference_" data-target="3447323">
                                                                                <i class="arrow-down"></i>
                                                                            </div>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-left">
                                                                        <div id="ord-details-preference_3447323" class="aditional-details">
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Specific Truck Features</div>
                                                                                <div class="ord-col-2">
                                                                                    No                                                                                </div>
                                                                                <div class="ord-col-3">
                                                                                    <span class="pull-right info"
                                                                                        title="Refrigerated, Dry van, Long-haul, Trucking-heavy-hauling, Inter-state, Intra-state, General freight, Flatbed, Over Dimensional, Truck-load, Dry-bulk">
                                                                                        <i class="fa fa-info "></i>
                                                                                    </span>
                                                                                </div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Specific Driver's Qualifications</div>
                                                                                <div class="ord-col-2">
                                                                                    No                                                                                </div>
                                                                                <div class="ord-col-3">
                                                                                    <span class="pull-right info"
                                                                                        title="HIPAA, TSA, Bonded, Commercial driver’s license">
                                                                                        <i class="fa fa-info"></i>
                                                                                    </span>
                                                                                </div>
                                                                            </div>

                                                                        </div>
                                                                    </div>
                                                                </div>

                                                                <div class="col-sm-6">

                                                                    <div class="ord-details-table-right">
                                                                        <div class="ord-col-1">Flat fee </div>
                                                                        <div class="ord-col-2">$ 7.14</div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="$4">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-table-right">
                                                                        <div class="ord-col-1">Base Miles Fee</div>
                                                                        <div class="ord-col-2">$ 0.00</div>
                                                                        <div class="ord-col-3">
                                                                            <span class="pull-right info"
                                                                                title="The first 3 miles cost $10 and every additional mile after costs $1.50">
                                                                                <i class="fa fa-info"></i>
                                                                            </span>
                                                                        </div>
                                                                    </div>

                                                                    <div class="ord-details-right">
                                                                        <div class="ord-det-item ord-details-table-subtotal">
                                                                            <div class="ord-col-1">Subtotal</div>
                                                                            <div class="ord-col-2">$ 7.14</div>
                                                                            <div class="ord-col-3"><span class="pull-right" title="The total cost of the order before additional costs"><i class="fa fa-info info"></i></span></div>
                                                                        </div>
                                                                        <div class="ord-det-item">
                                                                            <div class="ord-col-1">Additional Cost</div>
                                                                            <div class="ord-col-2"></div>
                                                                            <div class="ord-col-3">
                                                                                <div class="orderSlideDown butonDetaliiComanda" data-type="ord-details-additional_" data-target="3447323">
                                                                                    <i class="arrow-down"></i>
                                                                                </div>
                                                                            </div>
                                                                        </div>

                                                                        <div id="ord-details-additional_3447323" class="aditional-details">
                                                                                                                                                            <div class="ord-det-item">
                                                                                    <div class="ord-col-1">Admin price adjustment</div>
                                                                                    <div class="ord-col-2">$ 4.28</div>
                                                                                    <div class="ord-col-3"><span class="pull-right info" title="This is the price adjustment applied by a Point Pickup Admin to the original flat fee"><i class="fa fa-info"></i></span></div>
                                                                                </div>
                                                                                                                                                                                                                                    <div class="ord-det-item">
                                                                                <div class="ord-col-1">Oversize & Overweight Fee</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="A fee of 50% the cost of order is assessed if the package weighs more than 35 lbs "><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Stop fee</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="A fee of $ is assessed for each additional stop during the route "><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">ASAP fee</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="A fee of $ is assessed for immediate pickup"><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Scan fee</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="A fee of $ is assessed if the package needs to be scanned"><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Additional Insurance</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="The cost of any additional insurance placed on the package"><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Night fee</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="An added fee for nighttime deliveries between __PM and __AM"><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                            <div class="ord-det-item">
                                                                                <div class="ord-col-1">Specific Driver's Match</div>
                                                                                <div class="ord-col-2">$ 0.00</div>
                                                                                <div class="ord-col-3"><span class="pull-right info" title="A fee of $ is assessed for selecting a specific driver "><i class="fa fa-info"></i></span></div>
                                                                            </div>
                                                                                                                                                                                                                                                                                                            </div>

                                                                        <div class="ord-det-item ord-det-item-total total-cost">
                                                                            <div class="ord-col-1">Total</div>
                                                                            <div class="ord-col-2"></div>
                                                                            <div class="ord-col-3">
                                                                            $ 11.42                                                                            </div>
                                                                            <div class="post-tip-cost">
                                                                                                                                                        </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>



                                                        </div>
                                                    </div>
                                            </div>
                                            <br />
                                        </div>
                                    </div>
                                </div>

                                <div class="mt20 mb20">
                                    <hr/>
                                </div>
                                <div class="table-holder-tactivity" data-oid="PK-8293046586" data-routeid='3447323'></div>
                            </div>
                                            </div>
                </div>

            </div>

        </div>

    </div>
</div>

<span id="dataBag"
      class="dataBag"
      data-rpoints='{"3447323":["38.9624028,-78.189266","38.961234,-78.229504"]}'
      data-orderid="3046586"
      data-pk="PK-8293046586"
      data-routeid="3447323"
      >
    <!-- :) -->
</span>


<div id="modal-onlinedrivers" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel1" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                <h4 class="modal-title">
                    Notified Pickup Partners for order #PK-8293046586-3447323                </h4>
            </div>
            <div class="modal-body">

            </div>
            <div class="modal-footer">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>
        </div>
    </div>
</div>


<div id="modal-offlinedrivers" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel2" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                <h4 class="modal-title">
                    Logged Out Pickup Partners for order #PK-8293046586-3447323                </h4>
            </div>

            <div class="modal-body">

            </div>
            <div class="modal-footer">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>

        </div>
    </div>
</div>


<div id="modal-signature" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">
                    Signature
                </h4>
            </div>

            <div class="modal-body">
                <p class="modal-customer_name">Customer name: <span id="signature_name"></span></p>
                <img src="signature/default_signature.png" id='img_signature_url' class="w100">
            </div>
            <div class="modal-footer">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>

        </div>
    </div>
</div>

<div id="modal-photo-proof" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header" style="border-bottom: 0 none;">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">
                    Photo Proof
                </h4>
            </div>

            <div class="modal-body">
                <img src="photo_proof/default_photo_proof.png" id='img_proof_url' style="display:block; margin-left:auto; margin-right:auto; max-width: 70%; max-height: 70%; width: 400px; height: 500px;">
            </div>
            <div class="modal-footer" style="border-top: 0 none;">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>

        </div>
    </div>
</div>

<div id="modal-id" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel3" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                <h4 class="modal-title">
                    ID Verification
                </h4>
            </div>

            <div class="modal-body">
                <div class="id-verification-text" style="white-space: pre-wrap;">

                </div>

            </div>
            <div class="modal-footer">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>

        </div>
    </div>
</div>

<div id="modal-barcodes" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel5" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                <h4 class="modal-title">
                    <span id="get_title"></span>
                </h4>
            </div>
            <div class="modal-body mb-barcodes">

            </div>
            <div class="modal-footer">
                <button class="btn default" data-dismiss="modal" aria-hidden="true">Close</button>
            </div>
        </div>
    </div>
</div>

<div id="modalNotifyDrivers" class="modal fade modalNotifyDrivers" tabindex="-1" role="dialog" aria-labelledby="modalNotifyDrivers" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body">
                <p>Are you sure you want send a new notification to drivers in the area?</p>
                <br>
                <a href="#" data-dismiss="modal" aria-label="Close"  class="btn green btn-outline">Cancel</a>
                <a href="#"class="btn green confirmNotifyDrivers">Confirm</a>
            </div>
        </div>
    </div>
</div>

<div id="modalNotifyDriversSuccess" class="modal fade modalNotifyDrivers" tabindex="-1" role="dialog" aria-labelledby="modalNotifyDrivers" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body">
                <i class="fa fa-check" aria-hidden="true"></i>
                <b>Success</b>
                <p>The notification has been sent to <b><span class="driversNotified"></span></b> drivers.</p>
                <a href="#" data-dismiss="modal" aria-label="Close"  class="btn green">OK</a>
            </div>
        </div>
    </div>
</div>

<div id="modalUnassignDriver-3447323" class="modal fade modalUnassignDriver-3447323" tabindex="-1" role="dialog" aria-labelledby="modalUnassignDriver-3447323" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body text-center">
                <p>Remove Driver</p>
                <p><a href="https://pointpickup.com/control-panel/deliveries/unassign/3447323" onclick="clickAndDisable(this);" class="btn btn-danger" style="width: 240px;">Remove - No Fee</a></p>
                <p>If you need to unassign this driver with a Standard Cancellation Fee ($7.50) or Flat Fee ($7.14), please log in to the B2B Gateway and use one of the following options while selected the specific cancellation fee:
                    <br>
                    Cancel & republish (if before Pickup Time) or <br>
                    Cancel-to-Republish (if after Pickup Time).
                </p>
                <a class="cbtn btn green" style="width: 240px; margin-bottom: 10px;" id="loginas" href="https://pointpickup.com/control-panel/deliveries/loginas/PK-8293046586/multiple/as-it-is/3447323" target="_blank">
                    Login As
                </a> <br>
                <a href="#" data-dismiss="modal" aria-label="Close" class="btn green btn-outline" style="width: 240px;">Cancel</a>
            </div>
        </div>
    </div>
</div>

<div id="modalUnassignDriverSuccess" class="modal fade modalUnassignDriverSuccess" tabindex="-1" role="dialog" aria-labelledby="modalUnassignDriverSuccess" aria-hidden="true" style="display: none;">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-body">
                <i class="fa fa-check" aria-hidden="true"></i>
                <b>Success</b>
                <p>Driver successfully removed!</p>
                <a href="#" data-dismiss="modal" aria-label="Close"  class="btn green">OK</a>
            </div>
        </div>
    </div>
</div>


<script type="text/javascript">
     var routesStatuses = [];

              routesStatuses[3447323] = "ORDER_ACTIVE";

    document.addEventListener('DOMContentLoaded', function (event) {

        var routeId = $(".route_id").attr("id").split("id_").pop();

        var track1 = function() {
            ajaxGetCoordsPerRoute(routeId);
        };
        track1();

        var interval1;

        var doInterval1 = function() {
            interval1 = setInterval(function () {
                track1();
            }, 30000);
        };
        doInterval1();

        var hidden, visibilityChange;
        if (typeof document.hidden !== "undefined") { // Opera 12.10 and Firefox 18 and later support
            hidden = "hidden";
            visibilityChange = "visibilitychange";
        } else if (typeof document.msHidden !== "undefined") {
            hidden = "msHidden";
            visibilityChange = "msvisibilitychange";
        } else if (typeof document.webkitHidden !== "undefined") {
            hidden = "webkitHidden";
            visibilityChange = "webkitvisibilitychange";
        }

        function handleVisibilityChange() {
            if (document[hidden]) {
                clearInterval(interval1);
            } else {
                //track1();
                doInterval1();
            }
        }

        // Warn if the browser doesn't support addEventListener or the Page Visibility API
        if (typeof document.addEventListener === "undefined" || hidden === undefined) {
            console.warn("This demo requires a browser, such as Google Chrome or Firefox, that supports the Page Visibility API.");
        } else {
            // Handle page visibility change
            document.addEventListener(visibilityChange, handleVisibilityChange, false);
        }

        $('.id_link').click(function (e) {
            e.preventDefault();
            if($('.order_batch').length) {
                $(".order_batch.active .id-verification-text").html($(this).next().html());

                $('.order_batch.active #modal-id').modal('show');
            } else {
                $(".id-verification-text").html($(this).next().html());

                $('#modal-id').modal('show');
            }
        });

        $('.show_barcodes_modal').click(function(e){
            e.preventDefault();

            if($('.order_batch').length) {
                $(".order_batch.active #get_title").text('Package Scan');
                $('.order_batch.active #modal-barcodes').modal('show');
            } else {
                $("#get_title").text('Package Scan');
                $('#modal-barcodes').modal('show');
            }

            var point_id = $(this).attr('point');
            $.get('https://pointpickup.com/control-panel/deliveries/ajax_getbarcodes', {point_id: point_id}, function(response){
                $('.mb-barcodes').html(response);
            });
        });

        $('#auto-unassign-toggle').removeAttr('disabled');
        $('#auto-unassign-toggle').change(function() {
            $('#auto-unassign-toggle').attr('disabled', '');
            $('.auto-unassign-slider.round').html('');
            if (this.checked) {
                window.location.href = "https://pointpickup.com/control-panel/deliveries/change_auto_unassign/3046586/enable";
            } else {
                window.location.href = "https://pointpickup.com/control-panel/deliveries/change_auto_unassign/3046586/disable";
            }
        });

        $('#substract-minutes-to-auto-unassign').click(function(){
            if ($(this).parent().siblings('input').val() > 5) {
                $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) - 5)
            } else {
                $(this).parent().siblings('input').val(5);
            }
        });

        $('#add-minutes-to-auto-unassign').click(function(){
            if ($(this).parent().siblings('input').val() > 0) {
                $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) + 5)
            } else {
                $(this).parent().siblings('input').val(5);
            }
        });

        $('#manual-remove-driver-3447323').click(function(){
            $('#modalUnassignDriver-3447323').modal('show');
        });
    });

     function startTimer(duration, display) {

         var timer = duration, hours, minutes, seconds;
         setInterval(function () {

             hours = Math.floor(timer / (60 * 60));
             minutes = Math.floor((timer / 60) % 60);
             seconds = Math.floor(timer % 60);

             hours = hours < 10 ? "0" + hours : hours;
             minutes = minutes < 10 ? "0" + minutes : minutes;
             seconds = seconds < 10 ? "0" + seconds : seconds;

             $(display).html(hours + ":" + minutes + ":" + seconds);

             if (--timer < 0) {
                 timer = duration;
                 location.reload();
             }
         }, 1000);
     }

     // disable subsequent clicks
     function clickAndDisable(link) {
         link.onclick = function(event) {
             event.preventDefault();
         }
     }
</script>                                                        <div id="chart-container" style="width:48%; height:300px;"></div>
                                                    </div>


                </div>
                <!-- END CONTENT BODY -->
            </div>
            <!-- END CONTENT -->
        </div>
        <!-- END CONTAINER -->
    </div>

    <!--[if lt IE 9]>
        <script src="https://pointpickup.com/assets/control-panel/plugins/respond.min.js"></script>
        <script src="https://pointpickup.com/assets/control-panel/plugins/excanvas.min.js"></script>
        <script src="https://pointpickup.com/assets/control-panel/plugins/ie8.fix.min.js"></script>
    <![endif]-->

    <!-- BEGIN CORE PLUGINS -->
    <script src="https://pointpickup.com/assets/control-panel/plugins/jquery.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/js.cookie.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/jquery-slimscroll/jquery.slimscroll.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/jquery.blockui.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/bootstrap-switch/js/bootstrap-switch.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/bootstrap-switch/js/bootstrap-switch.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/bootbox/bootbox.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/select2/js/select2.full.min.js" type="text/javascript"></script>
    <!-- END CORE PLUGINS -->

    <!-- BEGIN THEME GLOBAL SCRIPTS -->
    <script src="https://pointpickup.com/assets/control-panel/scripts/app.min.js" type="text/javascript"></script>
    <!-- END THEME GLOBAL SCRIPTS -->

    <!-- BEGIN THEME LAYOUT SCRIPTS -->
    <script src="https://pointpickup.com/assets/control-panel/layout/scripts/layout.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/layout/scripts/demo.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/layout/scripts/quick-sidebar.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/layout/scripts/quick-nav.min.js" type="text/javascript"></script>
    <!-- END THEME LAYOUT SCRIPTS -->



    <script src="https://pointpickup.com/assets/control-panel/plugins/moment.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/plugins/bootstrap-daterangepicker/daterangepicker.min.js" type="text/javascript"></script>
    <script src="https://pointpickup.com/assets/control-panel/scripts/flatpickr.min.js" type="text/javascript"></script>

    <script>
        var GOOGLE_MAPS_API = 'AIzaSyBqUDh7eRBREObGqka7ovospf3IlP8IwB4';
    </script>

    <script type="text/javascript">
        if(/MSIE \d|Trident.*rv:/.test(navigator.userAgent)){
            document.write('<script src="https://pointpickup.com/assets/control-panel/scripts/compiled/main.js?v=2020090722" type="text/javascript" ><\/script>');
            document.write('<script src="https://pointpickup.com/assets/control-panel/scripts/compiled/upcoming.js?v=2020090722" type="text/javascript"><\/script>');
        } else {
            document.write('<script src="https://pointpickup.com/assets/control-panel/scripts/main.js?v=2020090722" type="text/javascript" ><\/script>');
            document.write('<script src="https://pointpickup.com/assets/control-panel/scripts/upcoming.js?v=2020090722" type="text/javascript"><\/script>');
        }
    </script>

    <script src="https://pointpickup.com/assets/control-panel/scripts/notification.js" type="text/javascript"></script>
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"NRJS-aeb285a862dbe7cc429","applicationID":"712421119","transactionName":"NFRTYBZQV0pXBkALXg0ecFcQWFZXGSFRDlgVVENdAUIWUFgDWw==","queueTime":0,"applicationTime":120,"atts":"GBNQFl5KREQ=","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
"""

#TODO: create unit tests of each function instead of these print debugs


# prints for "unit testing" the functions until unit tests are implemented
# print(find_price(html))
# print(find_company_name(html))
# print(find_drvr_name(html))
# print(find_dist(html))
#print(find_store_adrs(html))