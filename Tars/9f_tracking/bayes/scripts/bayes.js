'use strict';

function bayesSend(data) {
  this.iframe = document.createElement('iframe')
  this.iframe.style.display = 'none'
  document.documentElement.appendChild(this.iframe)
  var url = this.url + '?' + bayesUtil.serializeParam(data)
  this.send(url, function() {
    console.log('bayes success!')
  })
}
bayesSend.prototype.url = 'http://active.bayescom.com:8085/active'
bayesSend.prototype.send = function(url, callback) {
  this.iframe.src = url
  this.iframe.onload = callback
}

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
  },
  sendActive: function(source_in)
  {
    var source = source_in 
    var auction = bayesUtil.getUrlParam('auction', window.location.href)
    var crid = bayesUtil.getUrlParam('crid', window.location.href)

    if(source && auction && crid) {
      var bayes = new bayesSend( {
        source: source,
        auction: auction,
        crid: crid
      })
    }else{
      console.log("source send failed:",source_in)
    }
  }
}

document.addEventListener('DOMContentLoaded', function(event) {
  bayesUtil.sendActive("9f_load")
})

function bayesActive(source_in)
{
  var escaped_source = escape(source_in)
  bayesUtil.sendActive(escaped_source)
}

