// Minimal frontend logic for cart and simple interactions
const Cart = {
  items: [],
  add(item) {
    const found = this.items.find(i => i.id == item.id)
    if (found) found.qty += 1
    else this.items.push({...item, qty:1})
    this.save()
    this.renderMini()
    this.renderCartList()
  },
  remove(id) {
    this.items = this.items.filter(i => i.id != id)
    this.save(); this.renderMini(); this.renderCartList()
  },
  changeQty(id, delta) {
    const it = this.items.find(i=>i.id==id)
    if(!it) return
    it.qty = Math.max(1, it.qty + delta)
    this.save(); this.renderMini(); this.renderCartList()
  },
  clear() { this.items = []; this.save(); this.renderMini(); this.renderCartList() },
  save() { localStorage.setItem('fd_cart', JSON.stringify(this.items)) },
  load() { this.items = JSON.parse(localStorage.getItem('fd_cart')||'[]') },
  totalCount(){ return this.items.reduce((s,i)=>s+i.qty,0) },
  totalPrice(){ return this.items.reduce((s,i)=>s + i.qty * (parseFloat(i.price)||0),0) },
  renderMini(){
    const el = document.getElementById('cart-count')
    if(el) el.textContent = this.totalCount()
  },
  renderCartList(){
    const el = document.getElementById('cart-list')
    if(!el) return
    if(this.items.length===0){ el.innerHTML = '<p class="muted">Keranjang kosong.</p>'; return }
    const rows = this.items.map(i=>`
      <div class="cart-row">
        <div class="cart-name">${i.name}</div>
        <div class="cart-qty">
          <button data-id="${i.id}" class="qty-btn qty-dec">-</button>
          <span>${i.qty}</span>
          <button data-id="${i.id}" class="qty-btn qty-inc">+</button>
        </div>
        <div class="cart-sub">Rp ${ (i.qty * (parseFloat(i.price)||0)).toFixed(0) }</div>
        <button data-id="${i.id}" class="btn small remove">Hapus</button>
      </div>
    `).join('')
    el.innerHTML = rows
    // attach handlers
    el.querySelectorAll('.qty-dec').forEach(b=>b.addEventListener('click',e=>{Cart.changeQty(e.target.dataset.id,-1)}))
    el.querySelectorAll('.qty-inc').forEach(b=>b.addEventListener('click',e=>{Cart.changeQty(e.target.dataset.id,1)}))
    el.querySelectorAll('.remove').forEach(b=>b.addEventListener('click',e=>{Cart.remove(e.target.dataset.id)}))
    // update payment total if present
    const totalEl = document.getElementById('payment-total')
    if(totalEl) totalEl.textContent = 'Rp ' + this.totalPrice().toFixed(0)
  }
}

document.addEventListener('DOMContentLoaded', ()=>{
  Cart.load(); Cart.renderMini(); Cart.renderCartList()

  document.querySelectorAll('.add-to-cart').forEach(btn=>{
    btn.addEventListener('click', e=>{
      const id = btn.dataset.id
      const name = btn.dataset.name
      const price = btn.dataset.price
      Cart.add({id,name,price})
    })
  })

  const orderForm = document.getElementById('order-form')
  if(orderForm){
    orderForm.addEventListener('submit', e=>{
      e.preventDefault()
      if(Cart.items.length===0){ alert('Keranjang kosong!'); return }
      // Simple submit: send POST to /order (backend should accept JSON)
      fetch('/order', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({cart:Cart.items, name: orderForm.name.value, address: orderForm.address.value, note: orderForm.note.value})
      }).then(r=>{
        if(r.ok){ Cart.clear(); alert('Pesanan dibuat'); window.location='/payment' }
        else alert('Gagal membuat pesanan')
      }).catch(()=>alert('Gagal menghubungi server'))
    })
  }

  const paymentForm = document.getElementById('payment-form')
  if(paymentForm){
    paymentForm.addEventListener('submit', e=>{
      e.preventDefault()
      // For demo: simply clear cart and show success
      Cart.clear(); alert('Pembayaran dicatat. Terima kasih!'); window.location='/'
    })
  }
})
