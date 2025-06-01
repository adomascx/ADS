// Shell rikiavimo įgyvendinimas
function shellSort(arr) {
    let n = arr.length;
    // Pradėti nuo tarpo, lygus n padalinta iš 2 suapvalinta žemyn
    let gap = Math.floor(n / 2);
    
    // Tolti, kol tarpas sumažėja iki 0
    while (gap > 0) {
        // Atlikti įterpimo rikiavimą elementams su dabartiniu tarpu
        for (let i = gap; i < n; i++) {
            const temp = arr[i];
            let j = i;
            // Perstumti anksčiau tarpu surikiuotus elementus, kol randama tinkama vieta arr[i]
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }
            arr[j] = temp;
        }
        // Sumažinti tarpą kitai iteracijai
        gap = Math.floor(gap / 2);
    }
    
    return arr;
}

// Pavyzdys, kaip naudoti:
const unsortedArray = [7, 8, 99, 2, 5, 12, 34, 2, 3, 1];
console.log("Unsorted Array:", unsortedArray);
const sortedArray = shellSort(unsortedArray.slice()); // Naudoti nesurikiuoto masyvo kopiją
console.log("Sorted Array:", sortedArray);