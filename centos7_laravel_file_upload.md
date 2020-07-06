## Laravel Uploaded File Process ( 라라벨 파일 업로드 처리 )


### step1 - disk config
```
# /app/config/filesystem.php
return [

    /*
    |--------------------------------------------------------------------------
    | Default Filesystem Disk
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default filesystem disk that should be used
    | by the framework. The "local" disk, as well as a variety of cloud
    | based disks are available to your application. Just store away!
    |
    */

    'default' => env('FILESYSTEM_DRIVER', 'local'),

    /*
    |--------------------------------------------------------------------------
    | Default Cloud Filesystem Disk
    |--------------------------------------------------------------------------
    |
    | Many applications store files both locally and in the cloud. For this
    | reason, you may specify a default "cloud" driver here. This driver
    | will be bound as the Cloud disk implementation in the container.
    |
    */

    'cloud' => env('FILESYSTEM_CLOUD', 's3'),

    /*
    |--------------------------------------------------------------------------
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Here you may configure as many filesystem "disks" as you wish, and you
    | may even configure multiple disks of the same driver. Defaults have
    | been setup for each driver as an example of the required options.
    |
    | Supported Drivers: "local", "ftp", "sftp", "s3"
    |
    */

    'disks' => [
    //----- diks 정보 추가 시작 --------------------------------------------------
        'custom_01' => [
            'driver' => 'local',
            'root' => '/home/laravel/public_html/uploadFiles',
        ],
    // - 필자는 custom_01 이라는 이름의 디스크를 정의하여 경로를 지정하였다.
    //----- diks 정보 추가 끝 --------------------------------------------------        
        'local' => [
            'driver' => 'local',
            'root' => storage_path('app'),
        ],

        'public' => [
            'driver' => 'local',
            'root' => storage_path('app/public'),
            'url' => env('APP_URL').'/storage',
            'visibility' => 'public',
        ],
        'ftp' => [
            'driver' => 'ftp',
            'host' => 'ftp.example.com',
            'username' => 'your-username',
            'password' => 'your-password',
            
            // Optional FTP Settings...
            // 'port' => 21,
            // 'root' => '',
            // 'passive' => true,
            // 'ssl' => true,
            // 'timeout' => 30,
        ],
        'sftp' => [
            'driver' => 'sftp',
            'host' => 'example.com',
            'username' => 'your-username',
            'password' => 'your-password',
            
            // Settings for SSH key based authentication...
            // 'privateKey' => '/path/to/privateKey',
            // 'password' => 'encryption-password',
            
            // Optional SFTP Settings...
            // 'port' => 22,
            // 'root' => '',
            // 'timeout' => 30,
        ],
        's3' => [
            'driver' => 's3',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION'),
            'bucket' => env('AWS_BUCKET'),
            'url' => env('AWS_URL'),
            'endpoint' => env('AWS_ENDPOINT'),
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Symbolic Links
    |--------------------------------------------------------------------------
    |
    | Here you may configure the symbolic links that will be created when the
    | `storage:link` Artisan command is executed. The array keys should be
    | the locations of the links and the values should be their targets.
    |
    */

    'links' => [
        public_path('storage') => storage_path('app/public'),
    ],

];
```
### step2 - Storage 모듈에 대한 사용선언
```

    # Storage 모듈에 대한 사용선언
    use Illuminate\Support\Facades\Storage;

```
### step3 - 파일 생성 
```
    # custom_01 디스크에
    # 저장할 파일명 : test.png
    # 업로드된 파일데이타 : $httpRrequest->file('upload_files')
    
//             echo "\n\n";
//             var_dump(  public_path() );
//             echo "\n\n";
//             var_dump(  app_path() );
//             echo "\n\n";
//             var_dump(  base_path() );
//             echo "\n\n";
//             var_dump(  storage_path() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->getFileInfo() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->getFilename() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->getPathname() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->extension() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->getBasename() );
//             echo "\n\n";
//             var_dump( $httpRrequest->file('upload_file')->getClientOriginalName() );
//             echo "\n\n";
//             Storage::disk('custom_01')->put('test.png' , $httpRrequest->file('upload_files') ) ;
//             $httpRrequest->file('upload_file')->store($SaveFilePath, 'custom_01');

```


