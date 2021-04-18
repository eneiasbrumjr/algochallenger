<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Working extends Model
{
    protected $fillable = ['name', 'start_date', 'finish_date', 'is_multilogin'];

    protected $dates = ['start_date', 'finish_date', 'last_answser_date'];

    public function students() {
        return $this->belongsToMany(User::class)->withPivot('ip');
    }

    public function problems() {
        return $this->hasMany(Problem::class);
    }
}
