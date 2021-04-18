<?php

namespace App;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Tymon\JWTAuth\Contracts\JWTSubject;

class User extends Authenticatable implements JWTSubject
{
    use Notifiable;

    protected const USER_ROLE_ADMIN = 'admin';
    protected const USER_ROLE_STAFF = 'staff';
    protected const USER_ROLE_STUDENT = 'student';

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'full_name', 'password', 'username', 'type'
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
        'last_login' => 'datetime',
        'last_logout' => 'datetime',
    ];

    /**
     * Get the identifier that will be stored in the subject claim of the JWT.
     *
     * @return mixed
     */
    public function getJWTIdentifier()
    {
        return $this->getKey();
    }

    /**
     * Return a key value array, containing any custom claims to be added to the JWT.
     *
     * @return array
     */
    public function getJWTCustomClaims()
    {
        return [];
    }

    public function workings() {
        return $this->belongsToMany(Working::class)->withPivot('ip');
    }

    public function isAdmin() {
        return $this->type == self::USER_ROLE_ADMIN;
    }

    public function isStaff() {
        return $this->type == self::USER_ROLE_STAFF;
    }

    public function isStudent() {
        return $this->type == self::USER_ROLE_STUDENT;
    }

    public function runs() {
        return $this->hasMany(Run::class, 'student_id');
    }
}
