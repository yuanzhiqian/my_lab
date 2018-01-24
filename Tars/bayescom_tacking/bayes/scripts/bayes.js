'use strict';

(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        return define(factory)
    } else if (typeof exports === 'object') {
        return module.exports = factory()
    } else {
        return root.bayes = factory()
    }
})(this, function() {
    var bayesUtil = {
        // serialize json object to string to put it in active_url
        serializeParam: function (param) {
            if (!param) {
                return ''
            }

            var qstr = []
            for (var key in param) {
                qstr.push(encodeURIComponent(key) + '=' + encodeURIComponent(param[key]))
            }

            return  qstr.join('&')
        },
        // get params from landing_url to get source, auctionid and crid
        getUrlParam: function (name, href, noDecode) {
            var re = new RegExp( '(?:\\?|#|&)' + name + '=([^&]*)(?:$|&|#)',  'i' ), m = re.exec(href)
            var ret = m ? m[1] : ''
            return !noDecode ? decodeURIComponent( ret ) : ret
        }
    }

    document.addEventListener('DOMContentLoaded', function(event) {
        var el = document.querySelectorAll('[data-bayes-source]')[0]

        if (el) {
            var source = el.getAttribute('data-bayes-source')
            var auction = bayesUtil.getUrlParam('auction', window.location.href)
            var crid = bayesUtil.getUrlParam('crid', window.location.href)

            if(source && auction && crid) {
                var bayes = new bayes(el, {
                    source: source,
                    auction: auction,
                    crid: crid
                })
            }

        } else {
            console.log('没有找到有 data-bayes-source 属性的元素')
        }
    })

    function bayes(el, data) {
        this.iframe = document.createElement('iframe')
        this.iframe.style.display = 'none'
        document.documentElement.appendChild(this.iframe)

        el = (typeof el === 'string') ? document.getElementById(el) : el
        el.addEventListener('click', function() {
            var url = this.url + '?' + bayesUtil.serializeParam(data)
            this.send(url, function() {
                console.log('bayes success!')
            })
        }.bind(this), false)
    }

    bayes.prototype.url = 'http://active.bayescom.com:8085/active'
    bayes.prototype.send = function(url, callback) {
        this.iframe.src = url
        this.iframe.onload = callback
    }

    return bayes
})
