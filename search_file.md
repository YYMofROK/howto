## Find files file names starting with "remi" in the '/root' directory
```

$ find /root -name "remi*" -type f

```

## Find files that contains the string'test' in the'/root' directory
```

$ find /root -type f | xargs grep -in 'test'

```

## Find files 0 bytes file in the '/root' directory
```

$ find /home -size 0 - type f

```
