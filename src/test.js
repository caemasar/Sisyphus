function PrefixInteger(num, n) {
    return (Array(n).join(0) + num).slice(-n);
}

for (i = 301; i <= 324; i++) {
    console.log("http://wailian.work/images/2019/01/05/" + PrefixInteger(i, 3) + ".jpg")
}