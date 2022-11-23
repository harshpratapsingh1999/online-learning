function applyCoupon() {

    let code = document.getElementById('coupon').value
    let allCoupon = JSON.parse(document.getElementById('all').value)
    for (let i = 0; i < allCoupon.length; i++) {
        if (allCoupon[i].code == code) {
           document.getElementById('coupon-cont').style.display = 'contents'
           document.getElementById('coupon-amt').innerHTML = "₹" + allCoupon[i].amount
           let total = document.getElementById('original').value
           console.log(total)
           document.getElementById('total').innerHTML = "₹" + (parseInt(total) - allCoupon[i].amount)
        }
    }
   }