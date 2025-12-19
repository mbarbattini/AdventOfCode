pub fn sum_repeated_in_range(lower: u64, upper: u64) -> u64 {
    let max_total_digits = digits(upper);
    let mut candidates: Vec<u64> = Vec::new();

    let lower128 = lower as u128;
    let upper128 = upper as u128;

    // d is the number of digits in the repeated block, r is the number of blocks
    for d in 1..=max_total_digits {
        for r in 2..=max_total_digits / d {
            // 10^d and 10^(d*r)
            let pow10_d = 10u128.pow(d as u32);
            let pow10_dr = 10u128.pow((d * r) as u32);

            let f = (pow10_dr - 1) / (pow10_d - 1);

            if f > upper128 {
                continue; // even k = 1 would be too big
            }

            let min_k128 = 10u128.pow((d - 1) as u32);
            let max_k128 = pow10_d - 1;

            let k_lo = ((lower128 + f - 1) / f).max(min_k128);
            let k_hi = (upper128 / f).min(max_k128);

            if k_lo > k_hi {
                continue;
            }
    
            for k in k_lo..=k_hi {
                let n = k * f;
                if n >= lower128 && n <= upper128 {
                    candidates.push(n as u64);
                }
            }
        }
    }

    candidates.sort_unstable();
    candidates.dedup();
    candidates.into_iter().sum::<u64>()
}

fn main() {
    println!("{}", sum_repeated_in_range(99, 115));
}
