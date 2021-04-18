<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Auth;

class Problem extends Model
{
    public function working() 
    {
        return $this->belongsTo(Working::class);
    }

    public function getZipPathAttribute()
    {
        return 'app/problems/' . $this->id . '/' . $this->base_file_name;
    }

    public function getDescriptionPathAttribute()
    {
        return 'app/problems/' . $this->id . '/description/' . $this->description_file_name;
    }

    public function runs()
    {
        if (Auth::user()->isStudent()) {
            return $this->hasMany(Run::class)->where('student_id', Auth::user()->id);
        }

        return $this->hasMany(Run::class);
    }
}
