let n = 0
let max = 1000
let pares = 0

for(let i=n; i < max; i++) {
    if(i % 2 != 0) {
        continue
    }
    pares++
}

console.log("Fim do programa")
console.log(`Quantidade de números pares: ${pares}`)

// while(n < max) {
//     console.log(`Aprendendo JavaScript - ${n}`)
//     if(n > 10) {
//         break
//     }
//     n++
// }
// console.log("Fim do programa")